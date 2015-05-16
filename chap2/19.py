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
        col1 = [e.split()[0] for e in sys.stdin.readlines()]
        c = Counter(col1)
        for line in c.most_common():
            print line[1], line[0]
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
