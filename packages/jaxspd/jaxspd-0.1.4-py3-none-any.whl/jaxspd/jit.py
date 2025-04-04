"""
JIT compatibility layer for older JAX versions
"""

import jax
from typing import Any, Callable, Optional, Union, Tuple

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
    Wrapper around JAX's jit decorator. By default, this is a direct passthrough to jax.jit.
    
    Args:
        fun: Function to be JIT-compiled
        static_argnums: Arguments to be treated as static
        static_argnames: Argument names to be treated as static
        donate_argnums: Arguments that can be donated to the computation
        inline: Whether to inline the function
        keep_unused: Whether to keep unused arguments
        device: Device to run the computation on
        backend: Backend to use for computation
        **kwargs: Additional arguments passed to jax.jit
    
    Returns:
        JIT-compiled function
    """
    return jax.jit(
        fun=fun,
        static_argnums=static_argnums,
        static_argnames=static_argnames,
        donate_argnums=donate_argnums,
        inline=inline,
        keep_unused=keep_unused,
        device=device,
        backend=backend,
        **kwargs
    ) 