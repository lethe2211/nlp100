#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from pickle_cache import PickleCache
import numpy as np
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
        top = count.most_common()
        rank = np.arange(len(top)) + 1
        freq = [f for w, f in top]
        plt.scatter(rank, freq, s=10)
        plt.title('Relationship between Rank and Value of Term Frequency')
        plt.xlabel('Rank (Logarithmic)')
        plt.ylabel('Term Frequency (Logarithmic)')
        plt.xscale('log')
        plt.yscale('log')
        plt.show()
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
