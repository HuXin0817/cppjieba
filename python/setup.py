from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
import pybind11

# 获取 pybind11 的包含目录
pybind11_includes = pybind11.get_include()

ext_modules = [
    Pybind11Extension(
        "cppjieba",
        ["binding.cpp"],
        include_dirs=[
            pybind11_includes,
            "../include",
            "../deps/limonp/include",
        ],
        define_macros=[("NDEBUG", None)],  # 关闭调试模式
        extra_compile_args=["-O3", "-DNDEBUG"],  # 编译优化
        extra_link_args=["-O3"],  # 链接优化
        language='c++',
        cxx_std=17,
    ),
]

setup(
    name="cppjieba",
    version="0.1.0",
    author="cppjieba",
    description="Python bindings for cppjieba",
    long_description="",
    ext_modules=ext_modules,
    install_requires=["pybind11>=2.6.0"],
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)
