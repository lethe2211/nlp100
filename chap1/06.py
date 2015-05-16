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
        s1 = 'paraparaparadise'
        s2 = 'paragraph'
        x = self.ngram(s1)
        y = self.ngram(s2)
        print x, y
        print set(x) & set(y)
        print set(x) | set(y)
        print set(x) - set(y)
        flag_x = False
        for i in range(len(x)):
            if x[i][0] == 's' and x[i][1] == 'e':
                flag_x = True
        print flag_x
        flag_y = False
        for i in range(len(y)):
            if y[i][0] == 's' and y[i][1] == 'e':
                flag_y = True
        print flag_y
        
        return None

    def ngram(self, seq):
        ans = []
        ans.append((None, seq[0]))
        for i in range(len(seq)-1):
            ans.append((seq[i], seq[i+1]))
        ans.append((seq[len(seq)-1], None))
        return ans

if __name__ == '__main__':
    m = Main()
    m.solve()
