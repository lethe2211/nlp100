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

        for sentence in text:
            for index, chunk in enumerate(sentence):
                if '名詞' in [m.pos for m in chunk.morphs]:
                    path = []
                    node = index
                    while True:
                        path.append(sentence[node].get_text())
                        node = sentence[node].dst
                        if node is None:
                            break
                    print ' -> '.join(path)
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
