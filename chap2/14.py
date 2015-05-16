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
        if len(sys.argv) != 2:
            return
        else:
            for line in sys.stdin.readlines()[:int(sys.argv[1])]:
                sys.stdout.write(line)
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
