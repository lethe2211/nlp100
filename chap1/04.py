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
        text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
        tokenizer = RegexpTokenizer(r'\w+')
        dic = {}
        for i, e in enumerate(tokenizer.tokenize(text)):
            if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
                dic[e[0]] = i + 1
            else:
                dic[e[:2]] = i + 1
        print dic
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
