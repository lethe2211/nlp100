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
            for m in sentence:
                if m['pos'] == '動詞':
                    print m['base']
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
