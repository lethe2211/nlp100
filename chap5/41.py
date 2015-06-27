#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from parse_cabocha_text_to_chunks import ParseCabochaTextToChunks

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        pcttc = ParseCabochaTextToChunks()
        text = pcttc.parse('neko.txt.cabocha')
        print text[7]
        
        return None
    
if __name__ == '__main__':
    m = Main()
    m.solve()
