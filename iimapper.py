#!/usr/bin/env python3
#sys for output
import sys
#re to tokenize/process words
from string import ascii_lowercase
def idmap(lyric,id,stop_words):
    """
    in: tuple of words in lyric, id : integer, stop_words : set of stopwords
    prints all unigrams to sys.stdout
    out: none
    """
    #remove all stopwords from lyric
    words = [w for w in lyric if w not in stop_words]
    for word in words:
        print("%s\t%d" % (word,id))
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
    stop_words = {'chorus','i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you','youd', "youre", "youve", "youll", "you'", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where','why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didnt", 'doesn', "doesnt", 'hadn', "hadnt", 'hasn', "hasnt", 'haven', "havent", 'isn', "isnt", 'ma', 'mightn', "mightnt", 'mustn', "mustnt", 'needn', "neednt", 'shan', "shant", 'shouldn', "shouldnt", 'wasn', "wasnt", 'weren', "werent", 'won', "wont", 'wouldn', "wouldnt"}
    input_generator = gen_input(sys.stdin)
    for line in input_generator:
        #songid = cnt
        cnt = line[0]
        #use wordlist except songid
        line = line[1:]
        idmap(line,cnt,stop_words)

if __name__ == "__main__":
    main()
