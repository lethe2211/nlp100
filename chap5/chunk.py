#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class Chunk(object):
    
    def __init__(self, morphs=[], dst=None, srcs=[]):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def get_text(self):
        return ''.join([m.surface for m in self.morphs if m.pos != '記号'])

    def append(self, morph):
        self.morphs.append(morph)
                
    def __str__(self):
        return '<text: {0}, srcs: {1}, dst: {2}>'.format(self.get_text(), str(self.srcs), self.dst)
    
    def __repr__(self):
        return self.__str__()

