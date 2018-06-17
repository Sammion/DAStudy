# -*- coding: utf-8 -*-
"""
Created on 2018/6/17

@author: Samuel
@Desc: 
@dependence: Noting
"""
import csv

with open("../../data/test01.csv") as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    for line in reader:
        print(line)



import json
with open("../../data/test01.json") as f:
    data = json.load(f)
    print(data)
    print(data["boolean"])
import nltk
nltk.download()
input_str = "Today is a good day. It is sunny. I want to go to study in the conpany."
from nltk.tokenize import sent_tokenize
all_sent = sent_tokenize(input_str)
print(all_sent)
