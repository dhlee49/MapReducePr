#!/usr/bin/env python3
import sys
#re to tokenize/process words
import re
#csv for reading the csv file
import csv
#argparse for input specification

def tokenize(lyric):
    #lower case it
    lyric = lyric.lower()
    #remove all .s at the end
    lyric = re.sub("\. |\.\n",' ',lyric)
    #remove all [],() , [1-9]x chunks (mostly verse 1 verse2 xxx) and ....
    lyric = re.sub(r"\([^)]*\)|\[[^]]*\]|[1-9]+x|\.\.+",'',lyric)
    #remove all non word except .(whatevers left here is for floating points)
    lyric = re.sub("[^a-z0-9\s.]",'',lyric)
    return lyric.split()
def main():
    """
    Read inputfile songdata.csv and read each line using csvReader
    and call map function for each lyric parsing as list of words
    """
    #open file as read-only binary file
    songdata = csv.DictReader(sys.stdin,delimiter =',',quotechar='"')
    inputf = open("input.txt","w")
    cnt = 0
    for line in songdata:
        cnt += 1
        inputf.write(str(cnt)+ " ");
        for w in tokenize(line['text']):
            inputf.write(w + " ");
        inputf.write("\n")
if __name__ == "__main__":
    main()
