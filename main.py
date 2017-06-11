#!/usr/bin/env python2.7
#coding=utf-8

import sen2word
import predict
import sys

def run(input_file,stop_file, sementic_file, neg_file, degree_file):
    f_in = open(input_file, "r")
    paragraph = f_in.read()
    f_in.close()
    wl = sen2word.sentence_split(paragraph)
    score = predict.paragraph_score(wl, input_file, stop_file, sementic_file, neg_file, degree_file)
    print score

def main():
    if len(sys.argv)<6:
        print "Usage: you can guess"
        sys.exit(1)
    input_file = sys.argv[1]
    stop_file = sys.argv[2]
    sementic_file = sys.argv[3]
    neg_file = sys.argv[4]
    degree_file = sys.argv[5]
    run(input_file,stop_file, sementic_file, neg_file, degree_file)

if __name__ =="__main__":
    main()
