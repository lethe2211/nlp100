#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from pickle_cache import PickleCache

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        with open('./neko.txt.mecab', 'r') as f:
            morphologies = []
            sentence = []
            for line in f.readlines():
                if line == 'EOS\n':
                    if len(sentence) > 0:
                        morphologies.append(sentence)
                        sentence = []
                else:
                    surface, result = line.split()
                    results = result.split(',')
                    sentence.append({'surface': surface, 'base': results[6], 'pos': results[0], 'pos1': results[1]})
            pc = PickleCache()
            pc.set('./neko.txt.mecab.pickle', morphologies)
            
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
