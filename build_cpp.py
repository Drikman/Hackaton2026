from setuptools import setup, Extension
import pybind11

# Recupere le chemin d'include de pybind11
include_dirs = [pybind11.get_include()]

ext_modules = [
    Extension(
        "math_utils",
        ["src/cpp_module/math_utils.cpp"],
        include_dirs=include_dirs,
        language="c++",
        extra_compile_args=["-std=c++11"],  # C++11 required
    ),
]

setup(
    name="math_utils",
    version="0.0.1",
    author="Your Name",
    description="A simple example using pybind11",
    ext_modules=ext_modules,
)
