#!/usr/bin/env python3
#sys for output
import sys
def skipgrammap(lyric,k,n):
    """
    in: tuple of words in lyrics, k skip and n grams
    print all 0-k skip n grams
    out: none
    """
    size = len(lyric)
    #iterate over all words
    for i in range(0,size):
        if i + n > size: #cannot build more n grams exit the print loop
            break
        skipsupport(lyric,lyric[i],i,k,n-1)
    return
def skipsupport(list,s,i,k,n):
    """
    in: tuple of words, incomplete skipgram s, position i, k skips, n words left to append
    print the word when n = 1(when you append the word to make complete n gram)
    or make recursive call where n > new n , i < new i
    out: None
    """
    if n > 0:
        #we have more than 1 grams to append
    #make recursive call to all 0 ~ k skipgrams
    # new s = prev_word + space + new word
        for j in range(1,k+2):
            if i + j < len(list):
                #append next word only if the index i+j is acceptable for the list
                skipsupport(list,s + " " + list[i+j],i + j, k, n-1)
            else:
                #i+ any value >= j are invalid index so break the loop
                break
    else: #we have appended n words, should be printed
        print("%s\t%d" % (s,1))
    return
def gen_input(input_file):
    """
    in: input file
    out: generator object for that input file
    """
    for line in input_file:
        yield line.split()

def main():
    """
    Read input from stdin and toss it to gen_input
    to obtain generator for stdin
    then apply unigram to each line
    """
    input_generator = gen_input(sys.stdin)
    for line in input_generator:
        #ignore first song id
        line = line[1:]
        skipgrammap(line,1,2)
if __name__ == "__main__":
    main()
