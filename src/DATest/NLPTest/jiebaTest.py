# -*- coding: utf-8 -*-
"""
Created on 9/2/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""
import jieba

content = "现如今，机器学习和深度学习带动人工智能飞速的发展，并在图片处理、语音识别领域取得巨大成功。"
# 精准分词
segs_1 = jieba.cut(content, cut_all=False)
print("*".join(segs_1))
# 全模式分词
segs_2 = jieba.cut(content, cut_all=True)
print("*".join(segs_2))

# 搜索引擎模式分词
segs_3 = jieba.cut_for_search(content)
print("*".join(segs_3))
# 封装成列表返回
segs_5 = jieba.__lcut(content)
print(segs_5)

# 获取词性
import jieba.posseg as psg

print([(x.word, x.flag) for x in psg.__lcut_internal(content)])

# count 词出现的次数
from collections import Counter

top5 = Counter(segs_5).most_common(5)
print(top5)

#
text = "铁甲网是中国最大的工程机械交易平台。"
print(jieba.__lcut(text))
jieba.add_word("铁甲网", 129)
print(jieba.__lcut(text))
