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
        t1 = 'abcEFG'
        t2 = '123456'
        t3 = 'hoge, fuga'
        print self.cipher(t1)
        print self.cipher(t2)
        print self.cipher(t3)

        return None

    def cipher(self, text):
        ans = ''
        for c in text:
            if c.islower():
                ans += unichr(219 - ord(c))
            else:
                ans += c
        return ans
    
if __name__ == '__main__':
    m = Main()
    m.solve()
