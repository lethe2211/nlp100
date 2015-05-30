#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from jawiki_country_parser import JawikiCountryParser
from basic_info_parser import BasicInfoParser
import requests

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
        base_url = 'http://en.wikipedia.org/w/api.php?'
        params = {'action': 'query', 'prop': 'imageinfo', 'format': 'json', 'iiprop': 'url', 'titles': 'Image:{0}'.format(dic[u'国旗画像'])}
        json = requests.get(base_url, params=params).json()
        print json['query']['pages']['23473560']['imageinfo'][0]['url']
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
