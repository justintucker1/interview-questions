#!/usr/bin/python3

from collections import defaultdict

def word_count(sentence):
    freqs = defaultdict(int) 

    def addWord(word):
        chars = []
        for c in word:
            if c.isalpha():
                chars.append(c.lower())
        freqs[''.join(chars)] += 1
    
    for word in sentence.split():
        addWord(word)
    return freqs
    


print(word_count("it's a mixed up crazy it's a world"))
