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
        text = 'I am an NLPer'
        print self.ngram(text.split())
        print [self.ngram(list(w)) for w in text.split()]
                    
        return None

    def ngram(self, seq):
        ans = []
        ans.append([None, seq[0]])
        for i in range(len(seq)-1):
            ans.append([seq[i], seq[i+1]])
        ans.append([seq[len(seq)-1], None])
        return ans
    
if __name__ == '__main__':
    m = Main()
    m.solve()
