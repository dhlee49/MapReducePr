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
        for word in line:
            print("%s\t%d" % (word,1))

if __name__ == "__main__":
    main()
