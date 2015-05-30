#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
import gzip
import json
import re

class BasicInfoParser(object):
    
    def __init__(self):
        self.basic_info = ''
        self.basic_info_dic = {}

    # 25.py
    def load(self, article):
        self.load_basic_info(article)
        self.convert_basic_info_into_dic()

    def load_basic_info(self, article):
        bi = re.compile(ur'(({{基礎情報.*\n)(|.*?\n)*(}}))', re.MULTILINE)
        match = bi.search(article)
        self.basic_info = match.group(0)

    def convert_basic_info_into_dic(self):
        for line in self.basic_info.split('\n'):
            line = line.strip()
            if line[0] == '|':
                key = line.split('=')[0].strip()[1:]
                value = line.split('=')[1].strip()
                self.basic_info_dic[key] = value

    def get_basic_info_dic(self):
        return self.basic_info_dic
    
    # 28.py
    def format(self):
        self.remove_stress_expression()
        self.remove_internal_link()
        self.remove_html_tag()
        self.remove_broken_html_tag()
        self.remove_lang()
        self.remove_file()
        
    # 26.py
    def remove_stress_expression(self):
        p = re.compile(ur'(\'{2,3}|\'{5})\s*(.[^\']+?)\s*\1')
        self.basic_info_dic = {k: p.sub(ur'\2', v) for k, v in self.basic_info_dic.items()}

    # 27.py
    def remove_internal_link(self):
        p = re.compile(ur'\[\[([^:]+?)(#.+?)?(\|.+)?\]\]')
        # return {k: p.sub(ur'\1', v) for k, v in self.basic_info_dic.items()}
        for k, v in self.basic_info_dic.items():
            try:
                self.basic_info_dic[k] = p.sub(lambda m: m.group(3)[1:], v)
            except:
                self.basic_info_dic[k] = p.sub(ur'\1', v)
        return self.basic_info_dic
    
    def remove_html_tag(self):
        p = re.compile(ur'<(\w+)>(.+?)</\1>|<(.+?)>')
        self.basic_info_dic = {k: p.sub(r'', v) for k, v in self.basic_info_dic.items()}

    def remove_broken_html_tag(self):
        p = re.compile(ur'<(.+?)$')
        self.basic_info_dic = {k: p.sub(r'', v) for k, v in self.basic_info_dic.items()}

    def remove_lang(self):
        p = re.compile(ur'{{lang\|(.+?)\|(.+?)}}')
        self.basic_info_dic = {k: p.sub(r'\2', v) for k, v in self.basic_info_dic.items()}
    
    def remove_file(self):
        p = re.compile(ur'\[\[(File|ファイル):(.+?)(\|(.*)){2,}\]\]')
        self.basic_info_dic = {k: p.sub(r'\2', v) for k, v in self.basic_info_dic.items()}
