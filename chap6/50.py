#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
import re

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        with open('nlp.txt', 'r') as f:
            text = []
            for line in f.readlines():
                if len(line) < 3:
                    text.append(line)
                else:
                    start = 0
                    for i in range(len(line)):
                        if line[i] in ['.', ';', ':', '?', '!'] and line[i+1] == ' ' and line[i+2].isupper():
                            text.append(line[start:i+1])
                            start = i + 2
                    text.append(line[start:])

        for sentence in text:
            print sentence.rstrip()
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
