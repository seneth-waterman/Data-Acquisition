from tfidf import *
import os
import pickle
from lxml import etree

"""
1. Get a list of all xml_files in the corpus (~/data/reuters-vol1-disk1-subset).
2. Get a list of texts for all files xml_files.
3. Get a list of tokenized text (list of list of tokens).
4. Save the tokenized corpus in ~/data/tok_corpus.pickle.
"""

directory_path = sys.argv[1]

# 1. Get a list of all xml_files in the corpus (~/data/reuters-vol1-disk1-subset).
directory = os.path.expanduser(directory_path)
xml_files = []
for elem in os.walk(directory):  # os.walk returns tuple, 3rd value is filename.
    xml_files = elem[2]

xml_file_names = []
for file in xml_files:
    xml_file_names.append(directory_path + '/' + file)

# 2. Get a list of texts for all files xml_files.
xml_content = []
for file in xml_file_names:
    xml_content.append(gettext(file))

# 3. Get a list of tokenized text (list of list of tokens)
tokens = []
nlp = spacy.load("en_core_web_sm")
for text in xml_content:
    tokens.append(tokenize(text, nlp))

# 4. Save the tokenized corpus in ~/data/tok_corpus.pickle.
pickle_file = os.path.expanduser("~/data/tok_corpus.pickle")
with open(pickle_file, 'wb') as file:
    pickle.dump(tokens, file)


