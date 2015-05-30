#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from jawiki_country_parser import JawikiCountryParser
from basic_info_parser import BasicInfoParser

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        jcp = JawikiCountryParser()
        article = jcp.get_article(u'イギリス')
        bip = BasicInfoParser()
        bip.load(article)
        bip.format()
        dic = bip.get_basic_info_dic()
        for k, v in dic.items():
            print k, v

        return None

    
if __name__ == '__main__':
    m = Main()
    m.solve()
