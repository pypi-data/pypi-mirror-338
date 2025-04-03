"""
Utility functions for JAX operations
"""

import jax
import jax.numpy as jnp
from typing import Any, Callable, Optional, Union, List, Tuple
import functools

def optimize_for_gpu(
    fun: Callable,
    *,
    memory_fraction: Optional[float] = None,
    allow_growth: bool = True,
) -> Callable:
    """
    Decorator to optimize a function for GPU execution.
    
    Args:
        fun: Function to optimize
        memory_fraction: Fraction of GPU memory to allocate
        allow_growth: Whether to allow GPU memory growth
    
    Returns:
        Optimized function
    """
    from .gpu import enable_gpu_optimizations
    
    enable_gpu_optimizations(memory_fraction, allow_growth)
    
    @jax.jit
    def optimized_fun(*args, **kwargs):
        return fun(*args, **kwargs)
    
    return optimized_fun

def batch_apply(
    fun: Callable,
    batch_size: int = 32,
    axis: int = 0,
) -> Callable:
    """
    Decorator to apply a function in batches.
    
    Args:
        fun: Function to apply in batches
        batch_size: Size of each batch
        axis: Axis along which to batch
    
    Returns:
        Batched function
    """
    @functools.wraps(fun)
    def batched_fun(*args, **kwargs):
        # Get the input array from the first argument
        x = args[0]
        if not isinstance(x, (jnp.ndarray, jax.Array)):
            return fun(*args, **kwargs)
        
        # Split into batches
        n = x.shape[axis]
        n_batches = (n + batch_size - 1) // batch_size
        batches = jnp.array_split(x, n_batches, axis=axis)
        
        # Process each batch
        results = []
        for batch in batches:
            batch_args = list(args)
            batch_args[0] = batch
            results.append(fun(*batch_args, **kwargs))
        
        # Concatenate results
        return jnp.concatenate(results, axis=axis)
    
    return batched_fun

def device_put(
    x: Any,
    device: Optional[Any] = None,
    backend: Optional[str] = None,
) -> Any:
    """
    Put an array on a specific device.
    
    Args:
        x: Array to put on device
        device: Device to put array on
        backend: Backend to use
    
    Returns:
        Array on specified device
    """
    return jax.device_put(x, device, backend)

def pmap(
    fun: Callable,
    *,
    devices: Optional[List[Any]] = None,
    backend: Optional[str] = None,
    axis_name: Optional[str] = None,
    donate_argnums: Union[int, Tuple[int, ...]] = (),
) -> Callable:
    """
    Parallel map a function across devices.
    
    Args:
        fun: Function to parallelize
        devices: List of devices to use
        backend: Backend to use
        axis_name: Name of the axis to parallelize over
        donate_argnums: Arguments that can be donated
    
    Returns:
        Parallelized function
    """
    return jax.pmap(
        fun,
        devices=devices,
        backend=backend,
        axis_name=axis_name,
        donate_argnums=donate_argnums,
    ) 