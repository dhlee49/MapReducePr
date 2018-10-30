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
    songdata = csv.reader(sys.stdin,delimiter =',',quotechar='"')
    for line in songdata:
        trigrammap(tokenize(line[3]))

if __name__ == "__main__":
    main()
