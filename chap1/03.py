#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from nltk.tokenize import RegexpTokenizer

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        print [len(e) for e in tokens]
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
