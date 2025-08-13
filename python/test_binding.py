#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试 cppjieba Python 绑定
"""

try:
    import cppjieba
    print("✓ 成功导入 cppjieba 模块")
except ImportError as e:
    print(f"✗ 导入失败: {e}")
    exit(1)

def test_basic_functionality():
    """测试基本功能"""
    print("\n=== 测试基本功能 ===")
    
    try:
        # 创建 Jieba 实例
        jieba = cppjieba.Jieba()
        print("✓ 成功创建 Jieba 实例")
        
        # 测试分词
        sentence = "我来到北京清华大学"
        words = jieba.Cut(sentence)
        print(f"✓ 分词结果: {words}")
        
        # 测试全模式分词
        words_all = jieba.CutAll(sentence)
        print(f"✓ 全模式分词: {words_all}")
        
        # 测试搜索引擎模式
        words_search = jieba.CutForSearch(sentence)
        print(f"✓ 搜索引擎模式: {words_search}")
        
        # 测试词性标注
        tags = jieba.Tag(sentence)
        print(f"✓ 词性标注: {tags}")
        
        # 测试关键词提取
        keywords = jieba.extractor.extract(sentence, topK=3, withWeight=True)
        print(f"✓ 关键词提取: {keywords}")
        
        return True
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        return False

def test_user_dict():
    """测试用户词典功能"""
    print("\n=== 测试用户词典功能 ===")
    
    try:
        jieba = cppjieba.Jieba()
        
        # 测试添加用户词
        result = jieba.InsertUserWord("清华大学", "n")
        print(f"✓ 添加用户词结果: {result}")
        
        # 测试查找
        found = jieba.Find("清华大学")
        print(f"✓ 查找结果: {found}")
        
        return True
        
    except Exception as e:
        print(f"✗ 用户词典测试失败: {e}")
        return False

def test_word_structure():
    """测试 Word 结构"""
    print("\n=== 测试 Word 结构 ===")
    
    try:
        jieba = cppjieba.Jieba()
        sentence = "这是一个测试句子"
        
        # 测试带偏移量的关键词提取
        words = jieba.extractor.extract_with_offsets(sentence, topK=3)
        print(f"✓ Word 结构: {words}")
        
        if words:
            word = words[0]
            print(f"✓ 第一个词: word='{word.word}', weight={word.weight}, offsets={word.offsets}")
        
        return True
        
    except Exception as e:
        print(f"✗ Word 结构测试失败: {e}")
        return False

if __name__ == "__main__":
    print("开始测试 cppjieba Python 绑定...")
    
    success = True
    success &= test_basic_functionality()
    success &= test_user_dict()
    success &= test_word_structure()
    
    if success:
        print("\n🎉 所有测试通过！")
    else:
        print("\n❌ 部分测试失败")
        exit(1)
