#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from jawiki_country_parser import JawikiCountryParser

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        jcp = JawikiCountryParser()
        print jcp.get_article(u'イギリス')
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
