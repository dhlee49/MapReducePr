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

def trigrammap(list_words):
    """
    in: list of words in lyrics
    prints all bigrams to sys.stdout
    out: none
    """
    pprev = None
    prev = None
    for word in list_words:
        if prev is not None and pprev is not None:
            print("%s %s %s\t%d" % (pprev,prev,word,1))
        pprev = prev
        prev = word
    return
def main():
    """
    Read inputfile songdata.csv and read each line using csvReader
    and call map function for each lyric parsing as list of words
    """
    #open file as read-only binary file
    parser = argparse.ArgumentParser(description = 'Trigram mapper : Takes datafile.csv(that resides in same directory)')
    parser.add_argument("data",type = argparse.FileType('r'), help = 'csvfile that has format {"artist","song(title)","link","text"}')
    args = parser.parse_args()
    songdata = csv.DictReader(args.data)
    for line in songdata:
        trigrammap(tokenize(line['text']))

if __name__ == "__main__":
    main()
