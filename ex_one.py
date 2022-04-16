import json
import preprocess

"""Reading the JSON file"""
with open('dataset_smaller.json') as f:
    data = [json.loads(line) for line in f]

"""Initializing the preprocess object"""
prep = preprocess.PreProcessing()

"""Execution of preprocessing on reviews_dataset data"""
data = prep.tokenize_data(data)
data = prep.casefold_data(data)
data = prep.stopwords_data(data)
data = prep.remove_delimiters(data)

print(data)