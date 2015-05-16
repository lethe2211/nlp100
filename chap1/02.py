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
        s1 = u'パトカー'
        s2 = u'タクシー'
        ans = ''
        i1 = 0
        i2 = 0
        while True:
            flg = False
            if i1 < len(s1):
                ans += s1[i1]
                i1 += 1
                flg = True
            if i2 < len(s2):
                ans += s2[i2]
                i2 += 1
                flg = True
            if not flg:
                break
        print ans
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
