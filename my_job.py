from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

"""Read the delimiters file. This file, however, will have to be turned into code."""
"""Read the stopwords file"""
with open('stopwords.txt') as f:
    global stopwords
    stopwords = f.read().splitlines()

"""Read the delimiters file. This file, however, will have to be turned into code."""
with open('delimiters.txt') as f:
    global delimiters
    delimiters = f.read().splitlines()

class MRChiSquareTest(MRJob):

    def mapper(self, _, line):
    # yield each word in the line
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)
    
    def reducer(self, word, counts):
    # sum the words but filter them for stopwords or delimiters
        if len(word) != 0 and word not in stopwords and any(x in word for x in delimiters) == False:
            yield (word, sum(counts))
       


if __name__ == '__main__':
    MRChiSquareTest.run()