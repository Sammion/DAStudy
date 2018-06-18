# -*- coding: utf-8 -*-
"""
Created on 2018/6/18

@author: Samuel
@Desc: 
@dependence: https://nlp.stanford.edu/software/stanford-postagger-2017-06-09.zip
"""
from nltk.tag.stanford import StanfordPOSTagger
import nltk
s = 'The tagger was originally written by Kristina Toutanova. '
print(nltk.pos_tag(s))
stan_tagger = StanfordPOSTagger('stanford-postagger-2017-06-09/models/english-bidirectional-distsim.tagger',
                                'stanford-postagger-2017-06-09/stanford-postagger-3.8.0.jar')
tokens = nltk.word_tokenize(s)
print(tokens)
print(stan_tagger.tag(tokens))


