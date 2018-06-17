# -*- coding: utf-8 -*-
"""
Created on 2018/6/17

@author: Samuel
@Desc: 
@dependence: Noting
"""
from nltk.metrics import edit_distance

a = edit_distance("rain", "shine")
b = edit_distance("good", "god")
print(a, b)
