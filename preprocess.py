from mimetypes import init
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')



class PreProcessing():
    def __init__(self):
        pass

    """Read the stopwords file"""
    with open('stopwords.txt') as f:
        global lines
        lines = f.read().splitlines()

    def tokenize_data(self, list):
        self.list = list
        for i in self.list:
            for key, value in i.items():
                i[key] = word_tokenize(str(i[key]))
        return self.list

    def casefold_data(self, list):
        self.list = list
        for i in self.list:
            for key, values in i.items():
                for x in range(len(values)):
                    values[x] = values[x].casefold()
        return self.list


    def stopwords_data(self, list):
        self.list = list
        for i in self.list:
            for key, values in i.items():
                for word in values:
                    if (word in lines) or (len(word) == 1):
                        values.remove(word)
        return self.list

    def remove_commas(self, list):
        self.list = list
        for i in self.list:
            for key, values in i.items():
                for word in values:
                    if word == ',':
                        values.remove(word)
        return self.list