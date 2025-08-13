cmake_minimum_required(VERSION 3.10)
project(cppjieba_python)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 查找 Python 和 pybind11
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

# 设置包含目录
include_directories(
    ${PROJECT_SOURCE_DIR}/../include
    ${PROJECT_SOURCE_DIR}/../deps/limonp/include
)

# 创建 Python 模块
pybind11_add_module(cppjieba binding.cpp)

# 设置目标属性
set_target_properties(cppjieba PROPERTIES
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED ON
)

# 安装
install(TARGETS cppjieba
    LIBRARY DESTINATION ${Python3_SITEARCH}
    RUNTIME DESTINATION ${Python3_SITEARCH}
)
