# -*- coding: utf-8 -*-
"""
Created on 2018/6/17

@author: Samuel
@Desc: 
@dependence: Noting
"""
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
pst = PorterStemmer()
lst = LancasterStemmer()
print(lst.stem("eating"))
print(pst.stem("shopping"))