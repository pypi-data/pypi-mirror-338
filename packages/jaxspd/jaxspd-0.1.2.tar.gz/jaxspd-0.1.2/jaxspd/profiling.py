"""
Profiling and debugging utilities for JAX
"""

import jax
import jax.numpy as jnp
from typing import Any, Callable, Optional, Dict, List
import functools
import time
import os
from contextlib import contextmanager

class Profiler:
    """Profiler for JAX operations"""
    
    def __init__(self):
        self.stats: Dict[str, List[float]] = {}
        self.current_operation: Optional[str] = None
        self.start_time: Optional[float] = None
    
    def start(self, operation: str) -> None:
        """Start profiling an operation"""
        self.current_operation = operation
        self.start_time = time.time()
    
    def stop(self) -> None:
        """Stop profiling the current operation"""
        if self.current_operation is None or self.start_time is None:
            return
        
        duration = time.time() - self.start_time
        if self.current_operation not in self.stats:
            self.stats[self.current_operation] = []
        self.stats[self.current_operation].append(duration)
        
        self.current_operation = None
        self.start_time = None
    
    def get_stats(self) -> Dict[str, Dict[str, float]]:
        """Get profiling statistics"""
        result = {}
        for operation, durations in self.stats.items():
            result[operation] = {
                "mean": sum(durations) / len(durations),
                "min": min(durations),
                "max": max(durations),
                "count": len(durations),
            }
        return result

def profile(
    fun: Callable,
    *,
    profiler: Optional[Profiler] = None,
) -> Callable:
    """
    Decorator to profile a function's execution time.
    
    Args:
        fun: Function to profile
        profiler: Optional Profiler instance
    
    Returns:
        Profiled function
    """
    if profiler is None:
        profiler = Profiler()
    
    @functools.wraps(fun)
    def profiled_fun(*args, **kwargs):
        profiler.start(fun.__name__)
        try:
            return fun(*args, **kwargs)
        finally:
            profiler.stop()
    
    return profiled_fun

@contextmanager
def debug_mode():
    """Context manager for enabling debug mode"""
    original_config = jax.config.jax_debug_nans
    jax.config.update("jax_debug_nans", True)
    try:
        yield
    finally:
        jax.config.update("jax_debug_nans", original_config)

def memory_tracker(
    fun: Callable,
    *,
    track_inputs: bool = True,
    track_outputs: bool = True,
) -> Callable:
    """
    Decorator to track memory usage of a function.
    
    Args:
        fun: Function to track
        track_inputs: Whether to track input memory
        track_outputs: Whether to track output memory
    
    Returns:
        Memory-tracked function
    """
    @functools.wraps(fun)
    def tracked_fun(*args, **kwargs):
        memory_stats = {}
        
        if track_inputs:
            input_memory = 0
            for arg in args:
                if isinstance(arg, (jnp.ndarray, jax.Array)):
                    input_memory += arg.size * arg.dtype.itemsize
            memory_stats["input_memory"] = input_memory
        
        result = fun(*args, **kwargs)
        
        if track_outputs:
            output_memory = 0
            if isinstance(result, (jnp.ndarray, jax.Array)):
                output_memory = result.size * result.dtype.itemsize
            elif isinstance(result, tuple):
                for r in result:
                    if isinstance(r, (jnp.ndarray, jax.Array)):
                        output_memory += r.size * r.dtype.itemsize
            memory_stats["output_memory"] = output_memory
        
        # Store memory stats in function attributes
        tracked_fun.memory_stats = memory_stats
        return result
    
    return tracked_fun

def check_numerical_stability(
    fun: Callable,
    *,
    tolerance: float = 1e-6,
) -> Callable:
    """
    Decorator to check numerical stability of a function.
    
    Args:
        fun: Function to check
        tolerance: Tolerance for numerical stability checks
    
    Returns:
        Stability-checked function
    """
    @functools.wraps(fun)
    def checked_fun(*args, **kwargs):
        result = fun(*args, **kwargs)
        
        if isinstance(result, (jnp.ndarray, jax.Array)):
            if jnp.any(jnp.isnan(result)) or jnp.any(jnp.isinf(result)):
                raise ValueError("Numerical instability detected: NaN or Inf values")
            
            if jnp.any(jnp.abs(result) > 1/tolerance):
                print("Warning: Large values detected, possible numerical instability")
        
        return result
    
    return checked_fun 