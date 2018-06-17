# -*- coding: utf-8 -*-
"""
Created on 2018/6/17

@author: Samuel
@Desc: 
@dependence: Noting
"""
from nltk.stem import WordNetLemmatizer
wlem = WordNetLemmatizer()
res = wlem.lemmatize("eaten")
print(res)