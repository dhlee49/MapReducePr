#!/usr/bin/env python3
#sys for output
import sys
def gen_input(input_file):
    """
    in: input file
    out: generator object for that input file
    """
    for line in input_file:
        yield line.split()

def trigrammap(lyric):
    """
    in: tuple of all words in lyrics
    prints all triigrams to sys.stdout
    out: none
    """
    pprev = None
    prev = None
    for word in lyric:
        if prev is not None and pprev is not None:
            print("%s %s %s\t%d" % (pprev,prev,word,1))
        pprev = prev
        prev = word
    return

def main():
    """
    Read input from stdin and toss it to gen_input
    to obtain generator for stdin
    then apply biigram to each line
    """
    input_generator = gen_input(sys.stdin)
    for line in input_generator:
        #ignore first song id
        line = line[1:]
        trigrammap(line)
if __name__ == "__main__":
    main()
