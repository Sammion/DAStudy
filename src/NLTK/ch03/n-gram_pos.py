# -*- coding: utf-8 -*-
"""
Created on 2018/6/18

@author: Samuel
@Desc: 
@dependence: Noting
"""
from nltk.corpus import brown
import nltk

tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
freq_tags = nltk.FreqDist(tags)
print(freq_tags.items())
print(len(freq_tags.items()))
brown_tagged_sents = brown.tagged_sents(categories='news')
default_tagger = nltk.DefaultTagger('NN')
print(default_tagger.evaluate(brown_tagged_sents))

from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger
from nltk.tag import TrigramTagger

train_data = brown_tagged_sents[:int(len(brown_tagged_sents) * 0.9)]
test_data = brown_tagged_sents[int(len(brown_tagged_sents) * 0.9):]
# The backoff tagger that should be used for this tagger.
unigram_tagger = UnigramTagger(train_data, backoff=default_tagger)
print(unigram_tagger.evaluate(test_data))

biggram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
print(biggram_tagger.evaluate(test_data))
trigram_tagger = TrigramTagger(train_data, backoff=biggram_tagger)
print(trigram_tagger.evaluate(test_data))