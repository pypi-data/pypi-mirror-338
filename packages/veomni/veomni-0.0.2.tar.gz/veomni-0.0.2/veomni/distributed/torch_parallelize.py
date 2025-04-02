# Copyright 2025 Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from collections import defaultdict
from functools import partial
from typing import Any, Callable, Dict, List, Optional, Union

import torch
import torch.nn as nn
from torch.distributed.fsdp import CPUOffload, FullyShardedDataParallel, MixedPrecision, ShardingStrategy
from torch.distributed.fsdp._runtime_utils import _lazy_init
from torch.distributed.fsdp.wrap import lambda_auto_wrap_policy
from torch.nn.parallel import DistributedDataParallel as DDP

from ..checkpoint import register_checkpoint_extension
from ..utils import logging
from ..utils.import_utils import is_torch_version_greater_than
from .parallel_state import get_parallel_state
from .utils import set_module_from_path


if is_torch_version_greater_than("2.4"):
    from torch.distributed._composable.fsdp import MixedPrecisionPolicy, fully_shard
    from torch.distributed.tensor.parallel import parallelize_module


logger = logging.get_logger(__name__)


def verbose_fsdp_grouping(model, prefix="", depth=0):
    indent = "    " * depth

    for name, child in model.named_children():
        if isinstance(child, FullyShardedDataParallel):
            module_names = [m_name for m_name, _ in child.named_modules()][1:]  # [1:] 排除自身
            strategy = child.sharding_strategy
            logger.info_rank0(f"{indent}├── [FSDP Group] {prefix}{name}")
            logger.info_rank0(
                f"{indent}│   ├── Sharding Strategy: {strategy}, Mixed Precision: {child.mixed_precision}"
            )
            logger.info_rank0(f"{indent}│   └── Contains Modules: {module_names}")

            verbose_fsdp_grouping(child, prefix=f"{prefix}{name}.", depth=depth + 1)
        else:
            verbose_fsdp_grouping(child, prefix=f"{prefix}{name}.", depth=depth)


def _create_init_fn(model: "nn.Module", device: Union[str, "torch.device"]) -> Callable[["nn.Module"], None]:
    """
    Gets tensor materialization function that supports shared parameters and buffers.
    Args:
        model (nn.Module): the top module that may include shared parameters / buffers.
        device (Union[str, torch.device]): the device to initialize parameters on.

    Returns:
        Callable[[nn.Module], None]: initialization method to materialize meta tensors on device.
    """
    param_occurrence = defaultdict(int)
    for _, param in model.named_parameters(remove_duplicate=False):
        param_occurrence[param] += 1

    duplicated_params = {param for param in param_occurrence.keys() if param_occurrence[param] > 1}
    materialized_params = {}

    def init_fn(module: "nn.Module"):
        """
        NOTE: we can't use nn.Module.to_empty() because it will create new parameters, breaking the
        connection of shared parameters, we also can't use torch.utils.swap_tensors becuase tensors are on
        different devices. Instead, we can only reset nn.Module._parameters to make it work.
        """
        for name, param in module.named_parameters(recurse=False):
            if param in duplicated_params:
                module._parameters[name] = materialized_params.setdefault(
                    param, nn.Parameter(torch.empty_like(param.data, device=device), requires_grad=param.requires_grad)
                )
            else:
                module._parameters[name] = nn.Parameter(
                    torch.empty_like(param.data, device=device), requires_grad=param.requires_grad
                )

    return init_fn


def build_parallelize_model(
    model: "nn.Module",
    sharding_plan: Optional[Dict[str, Any]] = None,
    enable_full_shard: bool = True,
    enable_mixed_precision: bool = True,
    enable_gradient_checkpointing: bool = True,
    basic_modules: Optional[List[str]] = None,
    **kwargs,
) -> "nn.Module":
    """
    Applies parallel strategies to the model.
    """
    parallel_state = get_parallel_state()
    fsdp_no_shard_states = None

    if not parallel_state.fsdp_enabled or parallel_state.dp_mode != "fsdp1":
        if kwargs.pop("enable_rank0_init", False):
            raise ValueError("Only FSDP1 training supports `enable_rank0_init`.")
        if kwargs.pop("enable_fsdp_offload", False):
            raise ValueError("Only FSDP1 training supports `enable_fsdp_offload`.")

    if enable_mixed_precision:  # upcast to float32 before feed it to optimizer
        model = model.float()

    if enable_gradient_checkpointing and hasattr(model, "gradient_checkpointing_enable"):
        logger.info_rank0("Enable gradient checkpointing.")
        model.gradient_checkpointing_enable(
            gradient_checkpointing_kwargs={"use_reentrant": kwargs.pop("enable_reentrant", True)}
        )

    if parallel_state.tp_enabled:
        logger.info_rank0("Apply tensor parallel to the model.")
        model = parallelize_module(
            model,
            device_mesh=parallel_state.tp_mesh,
        )

    if parallel_state.ep_enabled:
        parallel_plan = model.get_parallel_plan()

        fqn2spec_info = parallel_plan.apply(model, parallel_state.ep_mesh)
        fsdp_no_shard_states_fqn_to_module = parallel_plan.get_fsdp_no_shard_info(model)

        fsdp_no_shard_states = list(fsdp_no_shard_states_fqn_to_module.values())
        fsdp_no_shard_states_fqn = list(fsdp_no_shard_states_fqn_to_module.keys())
        logger.info_rank0(
            f"Apply expert parallel to the model successfully.\nEP no shard states in FSDP: {fsdp_no_shard_states_fqn}."
        )
    else:
        fqn2spec_info = None
        fsdp_no_shard_states = None
        fsdp_no_shard_states_fqn = None

    if parallel_state.fsdp_enabled:
        logger.info_rank0(f"Apply data parallel to the model: {parallel_state.dp_mode}.")
        if parallel_state.dp_mode == "fsdp2":
            fsdp_kwargs = {
                "mesh": parallel_state.fsdp_mesh,
                "reshard_after_forward": enable_full_shard,
                **kwargs.pop("fsdp_kwargs", {}),
            }
            if enable_mixed_precision:
                logger.info_rank0("Enable mixed precision training.")
                mp_policy = MixedPrecisionPolicy(
                    param_dtype=torch.bfloat16,
                    reduce_dtype=torch.float32,
                    output_dtype=torch.bfloat16,
                )
                fsdp_kwargs["mp_policy"] = mp_policy

            ignore_modules_in_mixed_precision = tuple()
            if hasattr(model, "get_ignore_modules_in_mixed_precision"):
                ignore_modules_in_mixed_precision = model.get_ignore_modules_in_mixed_precision()

            def apply_fsdp_to_decoder_blocks(module: "nn.Module") -> None:
                if module.__class__.__name__ in basic_modules or module.__class__ in ignore_modules_in_mixed_precision:
                    logger.debug(f"Apply FSDP2 to {module.__class__.__name__}.")
                    if module.__class__ in ignore_modules_in_mixed_precision:
                        fully_shard(module, **{k: v for k, v in fsdp_kwargs.items() if k != "mp_policy"})
                    else:
                        fully_shard(module, **fsdp_kwargs)

            if basic_modules:
                model.apply(apply_fsdp_to_decoder_blocks)

            fully_shard(model, **fsdp_kwargs)

        elif parallel_state.dp_mode == "fsdp1":
            wrap_policy = partial(
                lambda_auto_wrap_policy, lambda_fn=lambda module: module.__class__.__name__ in basic_modules
            )

            fsdp_kwargs = {
                "auto_wrap_policy": wrap_policy,
                "ignored_states": fsdp_no_shard_states,
                "device_id": torch.cuda.current_device(),
                "sharding_strategy": ShardingStrategy.FULL_SHARD if enable_full_shard else ShardingStrategy.NO_SHARD,
                "device_mesh": parallel_state.fsdp_mesh,
                **kwargs.pop("fsdp_kwargs", {}),
            }

            if enable_mixed_precision:
                logger.info_rank0("Enable mixed precision training.")
                mixed_precision = MixedPrecision(
                    param_dtype=torch.bfloat16,
                    reduce_dtype=torch.float32,
                    buffer_dtype=torch.float32,
                )
                if hasattr(model, "get_ignore_modules_in_mixed_precision"):
                    mixed_precision._module_classes_to_ignore += model.get_ignore_modules_in_mixed_precision()

                fsdp_kwargs["mixed_precision"] = mixed_precision

            if kwargs.pop("enable_rank0_init", False):
                logger.info_rank0("Enable rank0-only initialization.")
                fsdp_kwargs["sync_module_states"] = True
                if get_parallel_state().global_rank != 0:
                    fsdp_kwargs["param_init_fn"] = _create_init_fn(model, device="cuda")

            if kwargs.pop("enable_fsdp_offload", False):
                logger.info_rank0("Enable offloading for parameters & gradients & optimizer states.")
                fsdp_kwargs["cpu_offload"] = CPUOffload(offload_params=True)

            if kwargs.pop("enable_forward_prefetch", False):
                fsdp_kwargs["forward_prefetch"] = True

            # FULLY_SHARD first
            model = FullyShardedDataParallel(model, **fsdp_kwargs)

            if fsdp_no_shard_states is not None:
                # apply NO_SHARD the ignored_states, but wrap into DDP
                logger.info_rank0(f"Apply NO_SHARD states on '{fsdp_no_shard_states_fqn}'.")
                fsdp_kwargs.pop("ignored_states", None)
                fsdp_kwargs.pop("auto_wrap_policy", None)
                fsdp_kwargs["sharding_strategy"] = ShardingStrategy.NO_SHARD
                for path, module in fsdp_no_shard_states_fqn_to_module.items():
                    set_module_from_path(model, path, FullyShardedDataParallel(module, **fsdp_kwargs))

            _lazy_init(model, model)

            # Apply fsdp extension to FSDP model
            save_hook_mesh = parallel_state.ep_mesh if parallel_state.ep_enabled else None
            logger.info_rank0("Register Checkpoints Extension hook to the model")
            register_checkpoint_extension(fsdp_model=model, device_mesh=save_hook_mesh, fqn2spec_info=fqn2spec_info)

            verbose_fsdp_grouping(model)
        else:
            ddp_kwargs = {"device_ids": [parallel_state.local_rank]}
            if enable_mixed_precision:
                logger.info_rank0("Enable mixed precision training.")
                mixed_precision = MixedPrecision(
                    param_dtype=torch.bfloat16,
                    reduce_dtype=torch.float32,
                    buffer_dtype=torch.bfloat16,
                )
                ddp_kwargs["mixed_precision"] = mixed_precision

            model = DDP(model, **ddp_kwargs)

    return model
