#!/usr/bin/env python3
#sys for output
import sys
#re to tokenize/process words
import re
#csv for reading the csv file
import csv
#argparse for input specification
import argparse
from string import ascii_lowercase
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
def tokenize(lyric):
    """
    in: lyric(element of row['text'])
    take whole lyric and convert it into list of words for analysis
    apply few cleaning processes tot remove punctuation & stopwords & errors(Minor focus on this)
    return: list of words in the lyric
    """
    lyric = lyric.lower()
    """
     tokenizer that will tokenize lyric('text') into words without punctuation
     it will split aphostrophe words into 2 seperate words but its okay
     as most of the time words with aphostrophe are non-main verbs(would,should,etc)
     non-main verbs are usually insignificant in most of the context and will be deleted
     e.g : would've = would ve but this is fine as we know stopwords will remove ve
     tweetTokenizer was producing very irregular words in lyric such as (8, numbers and was dist
    """
    #apply tokenizer
    tokenizer1= RegexpTokenizer("[a-z]+")
    words = tokenizer1.tokenize(lyric)
    #convert list of stopwords to set of stopwords for faster access
    en_stopwords = set(stopwords.words('english'))
    #we remove stopwords in words
    #and add few words that were in the words_lyric for cleaner process
    en_stopwords.add('chorus')
    #single letters aren't really words :)
    for c in ascii_lowercase:
        en_stopwords.add(c)

    words_lyric = [w for w in words if not w in en_stopwords]

    #postProcess of words_lyric
    words_lyric = preProcess(words_lyric)

    return words_lyric

def process(songcsv):
    """
    in: csvDictReader(csvfile)
    return: these are returned in sinlge function to reduce repeated csv read
            set of unique artists
            dictionary of artist : number of songs by artist
                          artist : sum of unique words in all songs
                          artist : number of unique words in all songs(By artist)
    """
    u_art = set()
    art_count = defaultdict(int)
    song_word = defaultdict(int)
    art_word = defaultdict(int)
    for row in songcsv:
        words = token_words(row['text'])
        unique_words = len(unique_set(words))
        #'link' is used as index instead of 'song'(title) as there might be a duplicate name for 'song'
        song_word[row['link']] += unique_words
        art_word[row['artist']] += unique_words
        art_count[row['artist']] += 1
        if row['artist'] not in u_art:
            u_art.add(row['artist'])
    return u_art,art_count,song_word,art_word

def preProcess(lyric):
    """
    in : lyric(in a form of list) that requires postProcessing, set of words in document so far for reference
    Words are processed in following ways
    1. word that has repetitive letters such as 'ya', 'yaaa' into single form('ya')
    2. for words that has length > 3 (if word length is greater than 4 usually 1 letter at the end does not change the meaning)
        if words - words.last or worst + [a-z] gives us a match with one of
    out: lyric into document
    """
    cnt = 0

    n_lyric = removerepeat(lyric)
    n2_lyric = removeNonWord(n_lyric)
    return n2_lyric
def removeNonWord(lyric):
    """
    in : word to be compared ,whole lyric, file for result output for debuggin
    return : lyric with no repeated words

    apply regular expressions [aeuioy] to make sure it is a proper word
        y was added for words such as 'cry', 'try', 'rhythm' that does not include vowel but may be a significant words
    """
    for w in lyric:
        regexp = re.compile('[aeuioy]')
        match = regexp.search(w)
        if not match:
            lyric.remove(w)
    return lyric
def removerepeat(lyric):
    """
    in : word to be compared ,whole lyric, file for result output for debuggin
    return : lyric with no repeated words

    apply regular expressions all alphabet+
    """
    #regstr is all repetition of single alphabet
    regstr =""
    for c in ascii_lowercase:
        regstr = regstr+ c+'+'+'|'
    regstr = regstr[:-1]
    regexp = re.compile(regstr)
    n_lyric = lyric
    for w in lyric:
        match = regexp.match(w)
        if match:
            if match.span()[1] == len(w):
                n_lyric.remove(w)
    return n_lyric
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
    songdata = csv.reader(sys.stdin,delimiter =',',quotechar='"')
    for line in songdata:
        unigrammap(tokenize(line[3]))

if __name__ == "__main__":
    main()
