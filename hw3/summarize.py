from tfidf import *
import os
import pickle

"""
1. Run compute_tok_corpus.py ~/data/reuters-vol1-disk1-subset to produce the pickle file with tokenized corpus.
2. Load ~/data/tok_corpus.pickle into a list.
3. Compute doc_freq of tokens.
4. Summarize the input xml input file (top 20).
5. Print the tfidf of top 20 words with three decimals of precision. Print only those words scoring >= 0.01. In your summarize() function, discard any terms with scores < 0.01.
"""

summarize_file = sys.argv[1]

pickle_file = os.path.expanduser("~/data/tok_corpus.pickle")
with open(pickle_file, 'rb') as file:
    tok_corpus = pickle.load(file)

N = len(tok_corpus)
n = 20
tfidf = summarize(summarize_file, doc_freq(tok_corpus), N, n)
for elem in tfidf:
    print(elem[0], round(elem[1], 3))
