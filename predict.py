#!/usr/bin/env python2.7
#coding=utf-8

import sen2word
import jieba
import codecs
import os


def classify_words(word_dics, sementic_file, neg_file, degree_file):
    f_in = open(sementic_file, "r")
    sen_dic = {}
    for line in f_in:
        line = line.rstrip()
        if len(line)>0:
            sen_dic[line.split(' ')[0].decode("utf8")] = float(line.split(' ')[1])
    f_in.close()

    f_in = open(neg_file, "r")
    neg_dic = {}
    for line in f_in:
        line = line.rstrip()
        if len(line)>0:
            neg_dic[line.decode("utf8")] = -1.0
    f_in.close()

    f_in = open(degree_file, "r")
    degree_dic = {}
    for line in f_in:
        line = line.rstrip()
        if len(line)>0:
            degree_dic[line.split(',')[0].decode("utf8")] = float(line.split(',')[1])
    f_in.close()

    sen_words = {}
    neg_words = {}
    degree_word = {}
    for word in word_dics.keys():
        if word in sen_dic and word not in neg_dic and word not in degree_dic:
            sen_words[word_dics[word]] = sen_dic[word]
        elif word  in neg_dic and word not in degree_dic:
            neg_words[word_dics[word]] = neg_dic[word]
        elif word in degree_dic:
            degree_word[word_dics[word]] = degree_dic[word]

    return sen_words, neg_words, degree_word


def paragraph_score(paragraph, input_file, stop_file, sementic_file, neg_file, degree_file):
    score = 0
    for sen in paragraph:
        sen_reg, new_dic = sen2word.sen2word(sen, stop_file)
        sen_words, neg_words, degree_words = classify_words(new_dic, sementic_file, neg_file, degree_file)
        score += sen_score(sen_words, neg_words, degree_words, sen)
    return score

def sen_score(sen_words, neg_words, degree_word, sen_reg):
    weight = 1
    score = 0
    sen_loc = -1

    for i in xrange(len(sen_reg)):
        if i in sen_words:
            sen_loc += 1
            score += weight * sen_words[i]
            if sen_loc <len(sen_words.keys()) -1:
                for j in xrange(sen_words.keys()[sen_loc], sen_words.keys()[sen_loc+1]):
                    if j in neg_words:
                        weight *= -1
                    elif j in degree_word:
                        weight *= degree_word[j]
        if sen_loc < len(sen_words.keys())-1:
                i = sen_words.keys()[sen_loc+1]
    return score
