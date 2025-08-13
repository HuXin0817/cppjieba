# cppjieba Python Bindings

这是 cppjieba 的 Python 绑定，使用 pybind11 构建。

## 安装依赖

首先安装必要的 Python 依赖：

```bash
pip install -r requirements.txt
```

## 构建

在 `python/` 目录下运行：

```bash
python setup.py build_ext --inplace
```

或者安装到系统：

```bash
python setup.py install
```

## 使用示例

```python
import cppjieba

# 创建 Jieba 实例
jieba = cppjieba.Jieba()

# 分词
sentence = "我来到北京清华大学"
words = jieba.Cut(sentence)
print(words)  # ['我', '来到', '北京', '清华大学']

# 全模式分词
words_all = jieba.CutAll(sentence)
print(words_all)  # ['我', '来到', '北京', '清华', '清华大学', '华大', '大学']

# 搜索引擎模式
words_search = jieba.CutForSearch(sentence)
print(words_search)  # ['我', '来到', '北京', '清华', '华大', '大学', '清华大学']

# 词性标注
tags = jieba.Tag(sentence)
print(tags)  # [('我', 'r'), ('来到', 'v'), ('北京', 'ns'), ('清华大学', 'nt')]

# 关键词提取
keywords = jieba.extractor.extract(sentence, topK=3, withWeight=True)
print(keywords)  # [('清华大学', 11.739204307083542), ('北京', 8.770167014113856), ('来到', 1.703297244400253e-03)]

# 添加用户词典
jieba.InsertUserWord("清华大学", "n")
jieba.InsertUserWord("北京", "ns")
```

## 主要功能

- **分词**: Cut, CutAll, CutForSearch, CutHMM, CutSmall
- **词性标注**: Tag, LookupTag
- **用户词典管理**: InsertUserWord, DeleteUserWord, LoadUserDict
- **关键词提取**: 支持带权重和不带权重的关键词提取
- **查找功能**: Find

## 注意事项

- 确保 cppjieba 的头文件路径正确
- 需要 C++11 或更高版本的编译器
- 在 macOS 上可能需要安装 Xcode 命令行工具
