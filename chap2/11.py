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
        ans = ''
        for line in sys.stdin.readlines():
            ans += line.replace('\t', ' ')
        print ans
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()