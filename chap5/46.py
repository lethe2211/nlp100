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
                    arguments = []
                    for src in chunk.srcs:
                        if '助詞' in [m.pos for m in sentence[src].morphs]:
                            argument = sentence[src].get_text()
                            case = [m.base for m in sentence[src].morphs if m.pos == '助詞'][-1]
                            arguments.append((case, argument))
                    if arguments:
                        arguments.sort()
                        print '{0}\t{1}\t{2}'.format(predicate, ' '.join([a[0] for a in arguments]), ' '.join([a[1] for a in arguments]))
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
