#!/bin/bash

# cppjieba Python 绑定构建脚本

set -e

echo "开始构建 cppjieba Python 绑定..."

# 检查 Python 版本
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
echo "检测到 Python 版本: $python_version"

# 检查是否在正确的目录
if [ ! -f "binding.cpp" ]; then
    echo "错误: 请在 python/ 目录下运行此脚本"
    exit 1
fi

# 检查上级目录结构
if [ ! -d "../include/cppjieba" ]; then
    echo "错误: 找不到 cppjieba 头文件目录"
    exit 1
fi

if [ ! -d "../deps/limonp/include" ]; then
    echo "错误: 找不到 limonp 依赖目录"
    exit 1
fi

# 安装依赖
echo "安装 Python 依赖..."
pip3 install -r requirements.txt

# 构建扩展
echo "构建 Python 扩展..."
python3 setup.py build_ext --inplace

echo "构建完成！"
echo ""
echo "测试绑定是否正常工作..."
python3 test_binding.py

echo ""
echo "如果测试通过，你可以："
echo "1. 使用 'python3 setup.py install' 安装到系统"
echo "2. 或者直接使用当前目录的 .so 文件"
echo ""
echo "使用示例："
echo "python3 -c \"import cppjieba; jieba = cppjieba.Jieba(); print(jieba.Cut('我来到北京清华大学'))\""
