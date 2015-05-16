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
        x = 12
        y = u'気温'
        z = 22.4
        print self.format_string(x, y, z)
        
        return None

    def format_string(self, x, y, z):
        return u'{x}時の{y}は{z}'.format(**{'x': x, 'y': y, 'z': z})
    
if __name__ == '__main__':
    m = Main()
    m.solve()
