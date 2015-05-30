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
        media = set()
        p1 = re.compile(ur'\[\[(File|ファイル):(.+?)(\|(.*)){2,}\]\]')
        for match in p1.findall(article):
            media.add(match[1])
        p2 = re.compile(ur'ファイル:(.+?)(\|(.*))+')
        for match in p2.findall(article):
            media.add(match[0])
        for elem in list(media):
            print elem
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
