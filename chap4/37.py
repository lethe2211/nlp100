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
        top10 = count.most_common(10)
        ind = np.arange(10)
        width = 0.35
        plt.bar(ind, [f for w, f in top10], width)
        plt.title('Top 10 of Term Frequency in Bocchan')
        plt.xlabel('Terms')
        plt.ylabel('Frequency')
        plt.xticks(ind + width / 2, [w.decode('utf-8') for w, f in top10])
        plt.show()
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
