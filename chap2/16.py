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
            n = int(sys.argv[1])
            filename = 'xaa'
            f = open('{0}'.format(filename), 'w')
            for index, line in enumerate(sys.stdin.readlines()):
                if index != 0 and index % n == 0:
                    f.close()
                    filename = self.next_string(filename)                    
                    f = open('{0}'.format(filename), 'w')
                f.write(line)
            f.close()
        
        return None

    def next_string(self, s):
        strip_zs = s.rstrip('z')
        if strip_zs:
            return strip_zs[:-1] + chr(ord(strip_zs[-1]) + 1) + 'a' * (len(s) - len(strip_zs))
        else:
            return 'a' * (len(s) + 1)

if __name__ == '__main__':
    m = Main()
    m.solve()
