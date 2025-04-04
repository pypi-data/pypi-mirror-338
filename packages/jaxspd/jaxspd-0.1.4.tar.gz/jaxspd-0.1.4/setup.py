from setuptools import setup, find_packages

# Read the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jaxspd",
    version="0.1.4",
    description="JAX Speed Optimizations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="JAX Contributor",
    author_email="jaxdev@example.com",
    url="https://github.com/jaxcontrib/jaxspd",
    packages=find_packages(),
    install_requires=[
        "jax>=0.4.13",
        "jaxlib>=0.4.13",
        "numpy>=1.20.0",
    ],
    extras_require={
        "gpu": ["cuda-python"],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
) 