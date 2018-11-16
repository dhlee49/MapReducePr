#!/usr/bin/env python3
import sys
def main():
    """
    in : stdin lines that has form word \t name
    argparser not used as it will create object for all stdin values
    which is not desirable
    """
    curr_word = None
    curr_cnt = 0
    s = None
    cnt = 0
    word = None
    for line in sys.stdin:
        line = line.strip()
        curr_word, curr_cnt = line.split(sep = '\t', maxsplit = 1)
        if curr_word == word: #sameword we want to check if id is different
            if curr_cnt != cnt: #different id add it to string
                s = s + ", " + curr_cnt
                cnt = curr_cnt
        else:
            # write result to STDOUT
            # and replace word & cnt with new version and empty s
            if word is not None:
                print('%s\t%s' % (word, s))
            cnt = curr_cnt
            word = curr_word
            s = curr_cnt
    if curr_word == word:
        print("{0:10s}\t{1:10s}".format(curr_word, s))
    return
if __name__ == "__main__":
    main()
