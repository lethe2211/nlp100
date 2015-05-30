#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json

class JawikiCountryParser(object):
    
    def __init__(self):
        pass

    def get_article(self, title):
        with gzip.open('jawiki-country.json.gz', 'r') as f:
            for line in f.readlines():
                data = json.loads(line)
                if data['title'] == unicode(title):
                    return data['text']

