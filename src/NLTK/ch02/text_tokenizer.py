# -*- coding: utf-8 -*-
"""
Created on 2018/6/17

@author: Samuel
@Desc: 
@dependence: Noting
"""
input_str = "Hi everyone! Hola gr8 &*$"
print(input_str.split())
from nltk.tokenize import word_tokenize, regexp_tokenize, wordpunct_tokenize, blankline_tokenize
output_str = word_tokenize(input_str)
print('word_tokenize: ')
print(output_str)
output_str = regexp_tokenize(input_str, pattern='\w+')
print('regexp_tokenize: ')
print(output_str)
output_str = regexp_tokenize(input_str, pattern='\d+')
print('regexp_tokenize: ')
print(output_str)
output_str = wordpunct_tokenize(input_str)
print('wordpunct_tokenize: ')
print(output_str)
output_str = blankline_tokenize(input_str)
print('blankline_tokenize: ')
print(output_str)
