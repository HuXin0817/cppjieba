#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cppjieba Python 绑定使用示例
"""

import cppjieba

def main():
    print("=== cppjieba Python 绑定使用示例 ===\n")
    
    # 创建 Jieba 实例
    jieba = cppjieba.Jieba()
    
    # 测试句子
    sentence = "我来到北京清华大学，这是一个美丽的校园"
    
    print(f"原句: {sentence}")
    print()
    
    # 1. 基本分词
    words = jieba.Cut(sentence)
    print(f"基本分词: {words}")
    
    # 2. 全模式分词
    words_all = jieba.CutAll(sentence)
    print(f"全模式分词: {words_all}")
    
    # 3. 搜索引擎模式
    words_search = jieba.CutForSearch(sentence)
    print(f"搜索引擎模式: {words_search}")
    
    # 4. HMM 模式
    words_hmm = jieba.CutHMM(sentence)
    print(f"HMM 模式: {words_hmm}")
    
    # 5. 词性标注
    tags = jieba.Tag(sentence)
    print(f"词性标注: {tags}")
    
    # 6. 关键词提取
    keywords = jieba.extractor.extract(sentence, topK=5, withWeight=True)
    print(f"关键词提取 (带权重): {keywords}")
    
    # 7. 关键词提取 (不带权重)
    keywords_no_weight = jieba.extractor.extract(sentence, topK=5, withWeight=False)
    print(f"关键词提取 (不带权重): {keywords_no_weight}")
    
    # 8. 带偏移量的关键词提取
    words_with_offsets = jieba.extractor.extract_with_offsets(sentence, topK=3)
    print(f"关键词提取 (带偏移量):")
    for word in words_with_offsets:
        print(f"  - '{word.word}': 权重={word.weight:.4f}, 位置={word.offsets}")
    
    print()
    
    # 9. 用户词典操作
    print("=== 用户词典操作 ===")
    
    # 添加用户词
    result = jieba.InsertUserWord("清华大学", "n")
    print(f"添加 '清华大学': {result}")
    
    # 查找词
    found = jieba.Find("清华大学")
    print(f"查找 '清华大学': {found}")
    
    # 添加带频率的用户词
    result2 = jieba.InsertUserWordWithFreq("美丽校园", 10, "n")
    print(f"添加 '美丽校园' (频率=10): {result2}")
    
    # 重新分词看效果
    new_words = jieba.Cut(sentence)
    print(f"添加用户词后的分词: {new_words}")
    
    print()
    print("=== 测试完成 ===")

if __name__ == "__main__":
    main()
