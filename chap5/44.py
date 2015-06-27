#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
import pydot
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

        sentence = text[7]      # As the dependency graph becomes too complex, we visualize only 8th sentence in this time
        edges = []
        for chunk in sentence:
            if chunk.dst is not None:
                edges.append((chunk.get_text(), sentence[chunk.dst].get_text()))
        g = pydot.graph_from_edges(edges)
        g.write_jpeg('44.jpg', prog='dot')
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
