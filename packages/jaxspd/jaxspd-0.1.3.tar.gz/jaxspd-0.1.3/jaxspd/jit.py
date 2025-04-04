"""
JIT compatibility layer for older JAX versions
"""

import functools
import jax
import jax.numpy as jnp
from typing import Any, Callable, Optional, Union, Tuple, List

def jit(
    fun: Optional[Callable] = None,
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
    Compatibility layer for JAX's jit decorator that works with older versions.
    
    Args:
        fun: Function to be JIT-compiled
        static_argnums: Arguments to be treated as static
        static_argnames: Argument names to be treated as static
        donate_argnums: Arguments that can be donated to the computation
        inline: Whether to inline the function
        keep_unused: Whether to keep unused arguments
        device: Device to run the computation on
        backend: Backend to use for computation
        **kwargs: Additional arguments passed to the underlying JIT implementation
    
    Returns:
        JIT-compiled function
    """
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            # Handle static arguments
            static_args = []
            if isinstance(static_argnums, int):
                static_args.append(args[static_argnums])
            else:
                static_args.extend(args[i] for i in static_argnums)
            
            # Handle static argument names
            if isinstance(static_argnames, str):
                static_args.append(kwargs[static_argnames])
            else:
                static_args.extend(kwargs[name] for name in static_argnames)
            
            # Create a function that only takes the dynamic arguments
            def dynamic_f(*dynamic_args):
                full_args = list(args)
                if isinstance(static_argnums, int):
                    full_args[static_argnums] = static_args[0]
                else:
                    for i, static_arg in zip(static_argnums, static_args):
                        full_args[i] = static_arg
                
                full_kwargs = dict(kwargs)
                if isinstance(static_argnames, str):
                    full_kwargs[static_argnames] = static_args[-1]
                else:
                    for name, static_arg in zip(static_argnames, static_args[len(static_argnums):]):
                        full_kwargs[name] = static_arg
                
                return f(*full_args, **full_kwargs)
            
            # Apply the underlying JIT implementation
            return jax.jit(
                dynamic_f,
                static_argnums=static_argnums,
                donate_argnums=donate_argnums,
                inline=inline,
                keep_unused=keep_unused,
                device=device,
                backend=backend,
                **kwargs
            )(*args)
        
        return wrapper
    
    if fun is None:
        return decorator
    return decorator(fun) 