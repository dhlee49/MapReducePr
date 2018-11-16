#!/usr/bin/env python3
import sys
import itertools
import operator
def reduce_generator(input_file):
    for line in input_file:
        yield line.split(sep = '\t', maxsplit = 1)
def main():
    """
    in : stdin lines that has form word \t name
    argparser not used as it will create object for all stdin values
    which is not desirable
    """
    curr_word = None
    curr_cnt = 0
    word = None
    # input comes from STDIN (standard input)
    red_gen = reduce_generator(sys.stdin)
    # groupby is one of itertool which takes in iterator and return 2 objects
    # 1 : key 2 : iterator for all members having same key
    for curr_word, group in itertools.groupby(red_gen, operator.itemgetter(0)):
        #group all words by key - itemgetter(0) where item[0] = word & item[1] = count)
        try:
            #aggregate all count for any curr_word
            total_count = sum(int(count) for curr_word, count in group)
            print ("%s\t%d" % (curr_word, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass
    return
if __name__ == "__main__":
    main()
