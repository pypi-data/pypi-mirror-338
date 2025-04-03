# JAXSPD

JAXSPD (JAX Speed Optimizations) is a Python package that provides speed optimizations for JAX. This package is particularly useful for users who need to optimize their JAX code for better performance.

## Features

- Optimized JIT compilation support
- Enhanced GPU support for NVIDIA GPUs
- Advanced optimization utilities
- Memory efficiency tools
- Profiling and debugging capabilities

## Installation

You can install JAXSPD using pip:

```bash
pip install jaxspd
```

For GPU support, install with the GPU extras:

```bash
pip install jaxspd[gpu]
```

## Usage

### Basic JIT Usage

```python
import jaxspd as jx

@jx.jit
def my_function(x):
    return x * 2 + 1

# The function will be JIT-compiled
result = my_function(5)
```

### GPU Optimizations

```python
import jaxspd as jx

# Enable GPU optimizations
jx.enable_gpu_optimizations()

# Your GPU-optimized code here
```

### Advanced Optimizations

```python
import jaxspd as jx

# Auto-JIT with memory optimization
@jx.auto_jit
def optimized_function(x):
    return jnp.sum(jnp.exp(x))

# Memory-efficient processing
@jx.memory_efficient(max_memory=1e9)  # 1GB max memory
def process_large_array(x):
    return jnp.mean(x, axis=0)

# Shape optimization
@jx.optimize_for_shape(static_shapes={"x": (1000, 1000)})
def matrix_operation(x):
    return jnp.dot(x, x.T)

# Operation fusion
@jx.fused_operations(fusion_level=2)
def fused_computation(x):
    return jnp.sum(jnp.exp(jnp.dot(x, x.T)))
```

## Requirements

- Python >= 3.8
- JAX >= 0.4.13
- JAXlib >= 0.4.13
- NumPy >= 1.20.0

For GPU support:
- CUDA-compatible GPU
- CUDA toolkit
- cuDNN

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 