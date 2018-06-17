# -*- coding: utf-8 -*-
"""
Created on 2018/6/17

@author: Samuel
@Desc: 
@dependence: pip install matplotlib
"""
import sys
import nltk
import urllib.request
import re
from bs4 import BeautifulSoup

response = urllib.request.urlopen('https://docs.python.org/2/library/re.html')
html = response.read().decode('UTF-8')
print(len(html))


def wordfreq(mystring):
    print(mystring)
    word_freq = {}
    for tok in mystring.split():
        if tok in word_freq:
            word_freq[tok] += 1
        else:
            word_freq[tok] = 1
    print(word_freq)


def word_freq(my_string):
    tokens = [tok for tok in re.split('\W+', html)]
    print("Total no of tokens: " + str(len(tokens)))
    print(tokens[0:10])


def word_nltk():
    soup = BeautifulSoup(html, 'lxml')
    clean = soup.getText()
    # clean = nltk.clean_html(html)
    tokens = [token for token in clean.split()]
    print(tokens[0:10])

    Freq_dist_nltk = nltk.FreqDist(tokens)
    for k, v in Freq_dist_nltk.items():
        print(str(k) + ":" + str(v))
    Freq_dist_nltk.plot(50, cumulative=False)


def main():
    my_str = "This is my first python program."
    word_freq(my_str)


if __name__ == '__main__':
    word_nltk()
