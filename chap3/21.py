#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from jawiki_country_parser import JawikiCountryParser
import re

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        jcp = JawikiCountryParser()
        article = jcp.get_article(u'イギリス')
        p = re.compile(r'\[\[Category\:.+\]\]')
        for line in article.split('\n'):
            if p.match(line):
                print line
            
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
