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
def idmap(list_words,id):
    """
    in: list of words in lyrics, id : integer
    prints all unigrams to sys.stdout
    out: none
    """
    for word in list_words:
        print("%s\t%d" % (word,id))
    return
def main():
    """
    Read inputfile songdata.csv and read each line using csvReader
    and call map function for each lyric parsing as list of words
    """
    #open file as read-only binary file
    cnt = 1
    songdata = csv.reader(sys.stdin,delimiter =',',quotechar='"')
    for line in songdata:
        idmap(tokenize(line[3]),cnt)
        cnt += 1
if __name__ == "__main__":
    main()
