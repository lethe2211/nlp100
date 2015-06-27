#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
from morph import Morph
from chunk import Chunk

class ParseCabochaTextToChunks(object):
    
    def __init__(self):
        pass

    def parse(self, filename):
        with open(filename, 'r') as f:
            sentences = []
            sentence = []
            chunk = None
            
            for line in f.readlines():
                if line.strip() == 'EOS':
                    self.set_srcs(sentence)
                    self.reset_dst(sentence)
                    sentences.append(sentence)
                        
                    sentence = []
                else:
                    if line.startswith('*'):
                        chunk = self.parse_chunk_header(line)
                        sentence.append(chunk)
                    else:
                        morph = self.parse_morph(line)
                        chunk.append(morph)
        return sentences

    def set_srcs(self, sentence):
        for index, chunk in enumerate(sentence):
            if chunk.dst != -1:
                sentence[chunk.dst].srcs.append(index)

    def reset_dst(self, sentence):
        if len(sentence) > 0:
            sentence[-1].dst = None
            
    def parse_chunk_header(self, line):
        chunk = Chunk()
        
        # FIXME: If you delete these lines, chunks.morphs references the old list of Morph        
        chunk.morphs = []
        chunk.srcs = []
        
        chunk.dst = int(line.split()[2][:-1])
        return chunk

    def parse_morph(self, line):
        surface, result = line.split()
        results = result.split(',')
        morph = Morph(surface, results[6], results[0], results[1])
        return morph
