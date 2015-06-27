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
            for j in range(len(sentence)-1):
                for k in range(len(sentence[j].morphs)-1):
                    if sentence[j].morphs[k].pos == '名詞' and sentence[j].morphs[k].pos1 == 'サ変接続' and sentence[j].morphs[k+1].pos == '助詞' and sentence[j].morphs[k+1].surface == 'を' and '動詞' in [m.pos for m in sentence[sentence[j].dst].morphs]:
                        predicate = sentence[j].get_text() + [m.base for m in sentence[sentence[j].dst].morphs if m.pos == '動詞'][0]
                        arguments = []
                        for src in list(set(sentence[j].srcs + sentence[sentence[j].dst].srcs) - set([j])):
                            if '助詞' in [m.pos for m in sentence[src].morphs]:
                                argument = sentence[src].get_text()
                                case = [m.base for m in sentence[src].morphs if m.pos == '助詞'][-1]
                                arguments.append((case, argument))
                        if arguments:
                            arguments.sort()
                            print '{0}\t{1}\t{2}'.format(predicate, ' '.join([a[0] for a in arguments]), ' '.join([a[1] for a in arguments]))
                        break
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
