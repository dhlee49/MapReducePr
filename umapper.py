#!/usr/bin/env python3
#sys for output
import sys
#re to tokenize/process words
import re
#csv for reading the csv file
import csv
#argparse for input specification
import argparse
def tokenize(lyric):
    """
    in: lyric as a sinlge string
    apply()
    return: list of words of the lyric
    """
    #prefix r makes escape char to be interpreted non literally
    #replace all words that's not consist of alphabet + nums [a-zA-Z0-9]
    # and words that ends with alph+nums with ''(empty string)
    lyric = re.sub(r'^\W+|\W+$','',lyric)
    #make lyric string into list of words
    words = re.split(r'\W+',lyric)
    return words
def unigrammap(list_words):
    """
    in: list of words in lyrics
    prints all unigrams to sys.stdout
    out: none
    """
    for word in list_words:
        print("%s\t%d" % (word,1))
    return
def main():
    """
    Read inputfile songdata.csv and read each line using csvReader
    and call map function for each lyric parsing as list of words
    """
    #open file as read-only binary file
    parser = argparse.ArgumentParser(description = 'Unigram mammper :Takes datafile.csv(that resides in same directory)')
    parser.add_argument("data",type = argparse.FileType('r'), help = 'csvfile that has format {"artist","song(title)","link","text"}')
    args = parser.parse_args()
    songdata = csv.DictReader(args.data)
    for line in songdata:
        unigrammap(tokenize(line['text']))

if __name__ == "__main__":
    main()
