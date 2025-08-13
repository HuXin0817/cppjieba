# cppjieba Python 绑定安装指南

## 系统要求

- Python 3.6 或更高版本
- C++11 兼容的编译器 (GCC 4.8+, Clang 3.3+, MSVC 2015+)
- 在 macOS 上需要 Xcode 命令行工具

## 安装方法

### 方法 1: 使用构建脚本 (推荐)

```bash
cd python
./build.sh
```

这个脚本会自动：
1. 检查系统环境
2. 安装 Python 依赖
3. 构建 Python 扩展
4. 运行测试验证

### 方法 2: 手动构建

#### 步骤 1: 安装依赖

```bash
cd python
pip install -r requirements.txt
```

#### 步骤 2: 构建扩展

```bash
python setup.py build_ext --inplace
```

#### 步骤 3: 测试

```bash
python test_binding.py
```

### 方法 3: 使用 CMake

```bash
cd python
mkdir build && cd build
cmake ..
make
```

## 安装到系统

构建成功后，可以选择安装到系统：

```bash
python setup.py install
```

或者使用 pip：

```bash
pip install .
```

## 验证安装

```python
import cppjieba

# 创建实例
jieba = cppjieba.Jieba()

# 测试分词
sentence = "我来到北京清华大学"
words = jieba.Cut(sentence)
print(words)  # 应该输出: ['我', '来到', '北京', '清华大学']
```

## 常见问题

### 1. 编译错误: 'pybind11/pybind11.h' file not found

**解决方案**: 确保已安装 pybind11
```bash
pip install pybind11
```

### 2. 找不到 cppjieba 头文件

**解决方案**: 确保在正确的目录结构下构建
```
objieba/
├── include/
│   └── cppjieba/
├── deps/
│   └── limonp/
└── python/
    └── binding.cpp
```

### 3. 链接错误

**解决方案**: 确保 C++ 标准库正确链接
```bash
export CXXFLAGS="-std=c++11"
python setup.py build_ext --inplace
```

### 4. 在 macOS 上的问题

**解决方案**: 安装 Xcode 命令行工具
```bash
xcode-select --install
```

## 开发调试

### 启用调试信息

```bash
python setup.py build_ext --inplace --debug
```

### 查看详细构建信息

```bash
python setup.py build_ext --inplace --verbose
```

## 性能优化

- 使用 `--inplace` 选项可以避免复制文件
- 在开发环境中使用 `--inplace`，在生产环境中使用 `install`

## 支持的功能

- ✅ 基本分词 (Cut, CutAll, CutForSearch, CutHMM, CutSmall)
- ✅ 词性标注 (Tag, LookupTag)
- ✅ 用户词典管理 (InsertUserWord, DeleteUserWord, LoadUserDict)
- ✅ 关键词提取 (支持权重和偏移量)
- ✅ 查找功能 (Find)
- ✅ 分隔符重置 (ResetSeparators)
