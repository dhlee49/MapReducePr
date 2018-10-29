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
    word = None
    for line in sys.stdin:
        line = line.strip()
        word, cnt = line.split(sep = '\t', maxsplit = 1)
        try:
        #try conversion of cnt(str) -> cnt(int)
            cnt = int(cnt)
        except ValueError:
        # count was not a number, ignore this line
            continue
        if curr_word == word:
            curr_cnt += cnt
        else:
            # write result to STDOUT
            if curr_word is not None:
                print('%s\t%d' % (curr_word, curr_cnt))
            curr_cnt = cnt
            curr_word = word
    if curr_word == word:
        print('%s\t%d' % (curr_word, curr_cnt))
    return
if __name__ == "__main__":
    main()
