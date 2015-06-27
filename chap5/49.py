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
            for i in range(len(sentence)-1):
                for j in range(i+1, len(sentence)):
                    if '名詞' in [m.pos for m in sentence[i].morphs] and '名詞' in [m.pos for m in sentence[j].morphs]:
                        # Get indices of morphs to be replaced by 'X' or 'Y'
                        index_x = []
                        index_x_flag = False
                        for index, m in enumerate(sentence[i].morphs):
                            if m.pos == '名詞':
                                index_x_flag = True
                                index_x.append(index)
                            else:
                                if index_x_flag:
                                    break
                        index_y = []
                        index_y_flag = False
                        for index, m in enumerate(sentence[j].morphs):
                            if m.pos == '名詞':
                                index_y_flag = True
                                index_y.append(index)
                            else:
                                if index_y_flag:
                                    break

                        # Get paths of syntax tree
                        path_i = []
                        path_j = []

                        node = i
                        while True:
                            path_i.append(node)
                            node = sentence[node].dst
                            if node is None:
                                break
                        node = j
                        while True:
                            path_j.append(node)
                            node = sentence[node].dst
                            if node is None:
                                break

                        # Display syntax tree
                        if set(path_i) >= set(path_j):
                            path_texts = self.get_replaced_texts(sentence, sorted(list(set(path_i) - set(path_j)) + [j]), i, j, index_x, index_y)
                            print ' -> '.join(path_texts)
                        else:
                            path_i_only_texts = self.get_replaced_texts(sentence, sorted(list(set(path_i) - set(path_j))), i, j, index_x, index_y)
                            path_j_only_texts = self.get_replaced_texts(sentence, sorted(list(set(path_j) - set(path_i))), i, j, index_x, index_y)
                            path_common_texts = self.get_replaced_texts(sentence, sorted(list(set(path_i) & set(path_j))), i, j, index_x, index_y)                            
                            print '{0} | {1} | {2}'.format(' -> '.join(path_i_only_texts), ' -> '.join(path_j_only_texts), ' -> '.join(path_common_texts))
                            
        return None

    def get_replaced_texts(self, sentence, path, i, j, replaced_morphs_i, replaced_morphs_j):
        texts = []
        for index in path:
            chunk_text = ''
            if index == i:
                for index_i, m in enumerate(sentence[index].morphs):
                    if index_i == replaced_morphs_i[0]:
                        chunk_text += 'X'
                    elif index_i in replaced_morphs_i:
                        pass
                    else:
                        chunk_text += m.surface
            elif index == j:
                for index_j, m in enumerate(sentence[index].morphs):
                    if index_j == replaced_morphs_j[0]:
                        chunk_text += 'Y'
                    elif index_j in replaced_morphs_j:
                        pass
                    else:
                        chunk_text += m.surface
            else:
                chunk_text += sentence[index].get_text()
            texts.append(chunk_text)
        return texts
    
if __name__ == '__main__':
    m = Main()
    m.solve()
