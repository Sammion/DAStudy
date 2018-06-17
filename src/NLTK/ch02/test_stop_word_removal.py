# -*- coding: utf-8 -*-
"""
Created on 2018/6/17

@author: Samuel
@Desc: 
@dependence: Noting
"""
from nltk.corpus import stopwords

stopwords = list(set(stopwords.words('english')))
text = "This is just a test for learning NLP."
clean_words = [word for word in text.split() if word not in stopwords]
print(clean_words)

import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import regexp_tokenize
import urllib
response = urllib.request.urlopen('https://docs.python.org/2/library/re.html')
html = response.read().decode('UTF-8')
soup = BeautifulSoup(html, 'lxml')
clean = regexp_tokenize(soup.getText(), pattern='\w+')
# clean = nltk.clean_html(html)
tokens = [token for token in clean]
freq_dist = nltk.FreqDist(tokens)
rare_word = freq_dist.keys()
after_rare_words = [word for word in tokens not in rare_word]
