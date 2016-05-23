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
        for line in sys.stdin:
            for word in line.split():
                print word
            print
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
