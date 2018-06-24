# -*- coding: utf-8 -*-
"""
Created on 2018/6/24

@author: Samuel
@Desc: 
@dependence: Noting
"""
from nltk.parse.stanford import StanfordParser

english_parser = StanfordParser('standford-parser.jar', 'standfordparser-3.8.0-models.jar')
english_parser.raw_parse_sents('This is the english parser test.')
