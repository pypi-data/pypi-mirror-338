"""
Advanced optimization utilities for JAX
"""

import jax
import jax.numpy as jnp
from typing import Any, Callable, Optional, Union, List, Tuple, Dict
import functools

def auto_jit(
    fun: Callable,
    *,
    static_argnums: Union[int, Tuple[int, ...]] = (),
    static_argnames: Union[str, Tuple[str, ...]] = (),
    donate_argnums: Union[int, Tuple[int, ...]] = (),
    inline: bool = False,
    keep_unused: bool = False,
    device: Optional[Any] = None,
    backend: Optional[str] = None,
    **kwargs
) -> Callable:
    """
    Enhanced JIT decorator that automatically handles static arguments and optimizes memory usage.
    
    Args:
        fun: Function to be JIT-compiled
        static_argnums: Arguments to be treated as static
        static_argnames: Argument names to be treated as static
        donate_argnums: Arguments that can be donated
        inline: Whether to inline the function
        keep_unused: Whether to keep unused arguments
        device: Device to run the computation on
        backend: Backend to use for computation
        **kwargs: Additional arguments
    
    Returns:
        Optimized function
    """
    from .jit import jit
    
    @jit(
        static_argnums=static_argnums,
        static_argnames=static_argnames,
        donate_argnums=donate_argnums,
        inline=inline,
        keep_unused=keep_unused,
        device=device,
        backend=backend,
        **kwargs
    )
    @functools.wraps(fun)
    def optimized_fun(*args, **kwargs):
        # Pre-allocate memory for large arrays
        args = list(args)
        for i, arg in enumerate(args):
            if isinstance(arg, (jnp.ndarray, jax.Array)) and arg.size > 1e6:
                args[i] = jax.device_put(arg, device)
        return fun(*args, **kwargs)
    
    return optimized_fun

def memory_efficient(
    fun: Callable,
    *,
    max_memory: Optional[float] = None,
    batch_size: Optional[int] = None,
) -> Callable:
    """
    Decorator to make a function memory efficient by automatically batching large operations.
    
    Args:
        fun: Function to optimize
        max_memory: Maximum memory usage in bytes
        batch_size: Optional fixed batch size
    
    Returns:
        Memory-efficient function
    """
    @functools.wraps(fun)
    def optimized_fun(*args, **kwargs):
        # Get the largest array from arguments
        largest_array = None
        max_size = 0
        for arg in args:
            if isinstance(arg, (jnp.ndarray, jax.Array)):
                size = arg.size * arg.dtype.itemsize
                if size > max_size:
                    max_size = size
                    largest_array = arg
        
        if largest_array is None:
            return fun(*args, **kwargs)
        
        # Calculate optimal batch size if not provided
        if batch_size is None and max_memory is not None:
            batch_size = int(max_memory / (max_size / largest_array.shape[0]))
        
        if batch_size is None:
            return fun(*args, **kwargs)
        
        # Apply batching
        from .utils import batch_apply
        return batch_apply(fun, batch_size=batch_size)(*args, **kwargs)
    
    return optimized_fun

def optimize_for_shape(
    fun: Callable,
    *,
    static_shapes: Optional[Dict[str, Tuple[int, ...]]] = None,
) -> Callable:
    """
    Decorator to optimize a function for specific input shapes.
    
    Args:
        fun: Function to optimize
        static_shapes: Dictionary mapping argument names to their expected shapes
    
    Returns:
        Shape-optimized function
    """
    @functools.wraps(fun)
    def optimized_fun(*args, **kwargs):
        if static_shapes is None:
            return fun(*args, **kwargs)
        
        # Convert args to kwargs for easier handling
        import inspect
        sig = inspect.signature(fun)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Check and optimize shapes
        for name, shape in static_shapes.items():
            if name in bound_args.arguments:
                arg = bound_args.arguments[name]
                if isinstance(arg, (jnp.ndarray, jax.Array)):
                    if arg.shape != shape:
                        # Reshape if needed
                        bound_args.arguments[name] = jnp.reshape(arg, shape)
        
        return fun(**bound_args.arguments)
    
    return optimized_fun

def fused_operations(
    fun: Callable,
    *,
    fusion_level: int = 2,
) -> Callable:
    """
    Decorator to fuse multiple operations for better performance.
    
    Args:
        fun: Function to optimize
        fusion_level: Level of operation fusion (1-3)
    
    Returns:
        Operation-fused function
    """
    @functools.wraps(fun)
    def optimized_fun(*args, **kwargs):
        # Apply JAX's XLA fusion
        with jax.jax_config.jit(level=fusion_level):
            return fun(*args, **kwargs)
    
    return optimized_fun 