"""
GPU optimization utilities for JAX
"""

import jax
import jax.numpy as jnp
from typing import Optional, Union, List
import os

def enable_gpu_optimizations(
    memory_fraction: Optional[float] = None,
    allow_growth: bool = True,
    per_process_gpu_memory_fraction: Optional[float] = None,
) -> None:
    """
    Enable GPU optimizations for JAX computations.
    
    Args:
        memory_fraction: Fraction of GPU memory to allocate
        allow_growth: Whether to allow GPU memory growth
        per_process_gpu_memory_fraction: Fraction of GPU memory to allocate per process
    """
    try:
        import cuda_python
        # Set CUDA environment variables
        if memory_fraction is not None:
            os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = str(allow_growth).lower()
            os.environ['TF_GPU_ALLOCATOR'] = 'cuda_malloc_async'
            if per_process_gpu_memory_fraction is not None:
                os.environ['TF_PER_PROCESS_GPU_MEMORY_FRACTION'] = str(per_process_gpu_memory_fraction)
    except ImportError:
        print("Warning: cuda-python not installed. GPU optimizations may not be available.")

def optimize_for_gpu(
    fun: callable,
    *,
    memory_fraction: Optional[float] = None,
    allow_growth: bool = True,
) -> callable:
    """
    Decorator to optimize a function for GPU execution.
    
    Args:
        fun: Function to optimize
        memory_fraction: Fraction of GPU memory to allocate
        allow_growth: Whether to allow GPU memory growth
    
    Returns:
        Optimized function
    """
    enable_gpu_optimizations(memory_fraction, allow_growth)
    
    @jax.jit
    def optimized_fun(*args, **kwargs):
        return fun(*args, **kwargs)
    
    return optimized_fun

def get_gpu_memory_info() -> dict:
    """
    Get information about GPU memory usage.
    
    Returns:
        Dictionary containing GPU memory information
    """
    try:
        import cuda_python
        # Implementation would go here
        return {
            "total_memory": 0,
            "free_memory": 0,
            "used_memory": 0,
        }
    except ImportError:
        return {
            "error": "cuda-python not installed",
            "total_memory": 0,
            "free_memory": 0,
            "used_memory": 0,
        } 