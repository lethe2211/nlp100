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
        pc = PickleCache()
        morphologies = pc.get('./neko.txt.mecab.pickle')
        for sentence in morphologies:
            for i in range(len(sentence)):
                if sentence[i]['surface'] == 'の' and 0 < i < len(sentence) - 1 and sentence[i-1]['pos'] == '名詞' and sentence[i+1]['pos'] == '名詞':
                    print sentence[i-1]['surface'] + sentence[i]['surface'] + sentence[i+1]['surface']
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
