# -*- coding: utf-8 -*-
"""
Created on 2018/6/24

@author: Samuel
@Desc: 
@dependence: Noting
"""
import nltk
from nltk.chunk.regexp import *

chunk_rules = ChunkRule("<.*>+", "chunk everything")
reg_parser = RegexpParser('''
NP: {<DT>? <JJ>* <NN>*} 
P: {<IN>} 
V: {<V.*>} 
PP: {<P> <NP>} 
VP: {<V> <NP|PP>*}
''')
test_sent = "Mr. Obama played a big role in the Health insurance bill."
test_sent_pos = nltk.pos_tag(nltk.word_tokenize(test_sent))
paresed_out = reg_parser.parse(test_sent_pos)
print(str(paresed_out))
