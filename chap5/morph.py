#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class Morph(object):

    def __init__(self, surface=None, base=None, pos=None, pos1=None):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '<surface: {0} base: {1}, pos: {2}, pos1: {3}>'.format(self.surface, self.base, self.pos, self.pos1)

    def __repr__(self):
        return self.__str__()
