"""
JAXSPD - JAX Speed Optimizations
"""

__version__ = "0.1.4"

from .jit import jit
from .gpu import enable_gpu_optimizations
from .utils import optimize_for_gpu, batch_apply, device_put, pmap
from .optimizations import (
    auto_jit,
    memory_efficient,
    optimize_for_shape,
    fused_operations,
)
from .profiling import (
    Profiler,
    profile,
    debug_mode,
    memory_tracker,
    check_numerical_stability,
)

__all__ = [
    # Core functionality
    "jit",
    "enable_gpu_optimizations",
    "optimize_for_gpu",
    
    # Utility functions
    "batch_apply",
    "device_put",
    "pmap",
    
    # Advanced optimizations
    "auto_jit",
    "memory_efficient",
    "optimize_for_shape",
    "fused_operations",
    
    # Profiling and debugging
    "Profiler",
    "profile",
    "debug_mode",
    "memory_tracker",
    "check_numerical_stability",
] 