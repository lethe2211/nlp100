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
        with open('col1.txt', 'r') as f1:
            with open('col2.txt', 'r') as f2:
                with open('merge.txt', 'w') as fmg:
                    while True:
                        line1 = f1.readline()
                        line2 = f2.readline()
                        if not (line1 or line2):
                            break
                        fmg.write(line1.strip() + '\t' + line2)
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
