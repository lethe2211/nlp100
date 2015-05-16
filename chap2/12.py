#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        col1 = []
        col2 = []
        for line in sys.stdin.readlines():
            elems = line.split()
            col1.append(elems[0])
            col2.append(elems[1])
        with open('col1.txt', 'w') as f1:
            f1.write('\n'.join(col1))
            f1.write('\n')
        with open('col2.txt', 'w') as f2:
            f2.write('\n'.join(col2))
            f2.write('\n')        
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
