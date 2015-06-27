#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from morph import Morph

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        with open('neko.txt.cabocha', 'r') as f:
            morphologies = []
            sentence = []
            for line in f.readlines():
                if line.strip() == 'EOS':
                    if len(sentence) > 0:
                        morphologies.append(sentence)
                        sentence = []
                elif not line.startswith('*'):
                    surface, result = line.split()
                    results = result.split(',')
                    sentence.append(Morph(surface, results[6], results[0], results[1]))
            print morphologies[2]
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
