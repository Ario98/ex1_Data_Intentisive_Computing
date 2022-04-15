from mrjob.job import MRJob
from mrjob.step import MRStep
import json
import preprocess

"""Reading the JSON file"""
with open('reviews_devset.json') as f:
    data = [json.loads(line) for line in f]

"""Initializing the preprocess object"""
Preprocessor = preprocess.PreProcessing()

"""Creating test data"""
mydict1 = {'fruits': ['BANANA', 'aPpLe', 'ORANGE', 'accordingly'],
         'vegetables': ['PEPPER', 'CARROT', 'accordingly', 'a'],
         'cheese': ['SWISS', 'CHEDDAR', 'bssASADe']}

mydict2 = {'fruits': ['v', 'ASDASLe', 'c'],
         'vegetables': ['PEASDAR', 'CAASDAST'],
         'cheese': ['anywhere', 'against', 'bsASDASDe']}

test_list = []
test_list.append(mydict1)
test_list.append(mydict2)

"""Execution of preprocessing on test data"""
print('Tokenizing data:')
test_list = Preprocessor.tokenize_data(test_list)
print(test_list)

print('Casefolding data:')
test_list = Preprocessor.casefold_data(test_list)
print(test_list)

print('Removing stopwords:')
test_list = Preprocessor.stopwords_data(test_list)
print(test_list)

print('Removing commas:')
test_list = Preprocessor.remove_commas(test_list)
print(test_list)

"""Execution of preprocessing on reviews_dataset data"""
data = Preprocessor.tokenize_data(data)
data = Preprocessor.casefold_data(data)
data = Preprocessor.stopwords_data(data)

print(data[3])
