#!/usr/bin/env python3
#sys for output
import sys
#re to tokenize/process words
import re
#csv for reading the csv file
import csv
#argparse for input specification
import argparse
from umapper import tokenize

def bigrammap(list_words):
    """
    in: list of words in lyrics
    prints all bigrams to sys.stdout
    out: none
    """
    prev = None
    for word in list_words:
        if prev is not None:
            print("%s %s\t%d" % (prev,word,1))
        prev = word
    return
def main():
    """
    Read inputfile songdata.csv and read each line using csvReader
    and call map function for each lyric parsing as list of words
    """
    #open file as read-only binary file
    parser = argparse.ArgumentParser(description = 'Bigram mapper : Takes datafile.csv(that resides in same directory)')
    parser.add_argument("data",type = argparse.FileType('r'), help = 'csvfile that has format {"artist","song(title)","link","text"}')
    args = parser.parse_args()
    songdata = csv.DictReader(args.data)
    for line in songdata:
        bigrammap(tokenize(line['text']))

if __name__ == "__main__":
    main()
