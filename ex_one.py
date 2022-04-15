from mrjob.job import MRJob
from mrjob.step import MRStep
import json
import preprocess

"""Reading the JSON file"""
with open('dataset_smaller.json') as f:
    data = [json.loads(line) for line in f]

"""Initializing the preprocess object"""
Preprocessor = preprocess.PreProcessing()

"""Execution of preprocessing on reviews_dataset data"""
data = Preprocessor.tokenize_data(data)
data = Preprocessor.casefold_data(data)
data = Preprocessor.stopwords_data(data)
data = Preprocessor.remove_delimiters(data)
print(data)