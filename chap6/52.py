#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from stemming.porter2 import stem
import re

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        for word in sys.stdin:
            word = re.sub('[.,:;!\?"\(\)]', '', word.rstrip())
            print '{0}\t{1}'.format(word, stem(word))
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
