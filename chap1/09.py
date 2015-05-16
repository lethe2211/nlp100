#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
import random
from collections import Counter, defaultdict
from nltk.tokenize import RegexpTokenizer

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        ans = []
        for word in text.split():
            if len(word) <= 4:
                ans.append(word)
                continue
            else:
                l = list(word[1:-1])
                random.shuffle(l)
                nword = word[0] + ''.join(l) + word[-1]
                ans.append(nword)
        print ' '.join(ans)
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
