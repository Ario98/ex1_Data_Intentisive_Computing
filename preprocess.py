import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')



class PreProcessing():
    def __init__(self):
        pass

    """Read the stopwords file"""
    with open('stopwords.txt') as f:
        global stopwords
        stopwords = f.read().splitlines()

    """Read the delimiters file. This file, however, will have to be turned into code."""
    with open('delimiters.txt') as f:
        global delimiters
        delimiters = f.read().splitlines()

    """Tokenization to unigrams using the nltk package"""
    def tokenize_data(self, provided_list):
        self.provided_list = provided_list
        for i in self.provided_list:
            for key, value in i.items():
                i[key] = word_tokenize(str(i[key]))
        return self.provided_list

    """Simple casefold of data by using string.casefold()"""
    def casefold_data(self, provided_list):
        self.provided_list = provided_list
        for i in self.provided_list:
            for key, values in i.items():
                for x in range(len(values)):
                    values[x] = values[x].casefold()
        return self.provided_list

    """Does it need to be changed as below since it is provided by the course?"""
    def stopwords_data(self, provided_list):
        self.provided_list = provided_list
        for i in self.provided_list:
            for key, values in i.items():
                for word in list(values):
                    if (word in stopwords) or (len(word) == 1):
                        values.remove(word)
        return self.provided_list

    """This function will have to be changed so it does not need the delimiter.txt file"""
    def remove_delimiters(self, provided_list):
        self.provided_list = provided_list
        for i in self.provided_list:
            for key, values in i.items():
                for word in list(values):
                    if any(x in word for x in delimiters):
                        values.remove(word)
        return self.provided_list