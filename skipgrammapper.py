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
def skipgrammap(list_words,k,n):
    """
    in: list of words in lyrics, k skip and n grams
    print all 0-k skip n grams
    out: none
    """
    size = len(list_words)
    #iterate over all words
    for i in range(0,size):
        if i + n > size: #cannot build more n grams exit the print loop
            break
        skipsupport(list_words,list_words[i],i,k,n-1)
    return
def skipsupport(list,s,i,k,n):
    """
    in: list of words, incomplete skipgram s, position i, k skips, n words left to append
    print the word when n = 1(when you append the word to make complete n gram)
    or make recursive call where n > new n , i < new i
    out: None
    """

    for j in range(1,k+2):
        #append next word only if we do not overflow the list
        if i + j < len(list):
            if n > 1:
                #we have more than 1 grams to append
                #make recursive call to all 0 ~ k skipgrams
                # new s = prev_word + space + new word
                skipsupport(list,s + " " + list[i+j],i + j, k, n-1)
            else: #we have appended n-1 words, next word should be printed
                print("%s\t%d" % (s + " " + list[i+j],1))
        else:
            break
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
        skipgrammap(tokenize(line['text']),1,2)

if __name__ == "__main__":
    main()
