#!/usr/bin/env python2.7
#coding=utf-8

import jieba
import codecs
import os

def sen2word(sentence, stop_file):
    seg_list = jieba.cut(sentence)
    seg_res = []
    for w in seg_list:
        seg_res.append(w)

    stop_words = []
    f_in = open(stop_file, "r")
    for line in f_in:
        stop_words.append(line.rstrip().decode("utf8")) #= 1

    new_sen = []
    word_dic = {}
    counter = 0
    for w in seg_res:
        if w not in stop_words:
            new_sen.append(w)
            word_dic[w] = counter
            counter+=1
    return new_sen, word_dic


def sentence_split(paragraph):
    list_ret = list()
    for s in paragraph.split('。'):
        s = s.rstrip()
        if len(s) >0:
            if '?' in s:
                list_ret.extend(s.rstrip().split('?'))
            elif '!' in s:
                list_ret.extend(s.rstrip().split('!'))
            else:
                list_ret.append(s.rstrip())
    return list_ret
