#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from pickle_cache import PickleCache
import matplotlib.pyplot as plt

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        pc = PickleCache()
        morphologies = pc.get('./neko.txt.mecab.pickle')
        words = [m['base'] for sentence in morphologies for m in sentence]
        count = Counter(words)
        plt.hist([f for w, f in count.items()], bins=100, range=(0, 10000))
        plt.title('Histogram of Term Frequency in Bocchan')
        plt.xlabel('Term Frequency')
        plt.ylabel('Freqency')
        plt.show()
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
