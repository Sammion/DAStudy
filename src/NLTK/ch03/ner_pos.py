# -*- coding: utf-8 -*-
"""
Created on 2018/6/18

@author: Samuel
@Desc: 
@dependence: Noting
"""
import nltk
from nltk import ne_chunk
sent = 'The tagger was originally written by Kristina Toutanova. He is working at Ebay in Shanghai office'
print(ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)), binary=True))
