#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools
import math
from collections import Counter, defaultdict
import cPickle

class PickleCache(object):
    
    def __init__(self):
        pass

    def get(self, filename):
        with open(filename, 'r') as f:
            unpickle = cPickle.Unpickler(f)
            value = unpickle.load()
            return value

    def set(self, filename, value):
        with open(filename, 'w') as f:
            pickle = cPickle.Pickler(f)
            pickle.dump(value)
