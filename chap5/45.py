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
            for chunk in sentence:
                if '動詞' in [m.pos for m in chunk.morphs]:
                    predicate = [m.base for m in chunk.morphs if m.pos == '動詞'][0]
                    cases = []
                    for src in chunk.srcs:
                        if '助詞' in [m.pos for m in sentence[src].morphs]:
                            case = [m.base for m in sentence[src].morphs if m.pos == '助詞'][-1]
                            cases.append(case)
                    if cases:
                        cases.sort()
                        print '{0}\t{1}'.format(predicate, ' '.join(cases))
                        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
