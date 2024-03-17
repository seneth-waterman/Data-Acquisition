import sys

import spacy
from lxml import etree
from collections import Counter
import string
import zipfile
import os
import numpy as np
import re

def gettext(xmlfile) -> str:
    """
    Parse xmltext and return the text from <title> and <text> tags
    """
    tree = etree.parse(xmlfile)
    root = tree.getroot()

    output = []
    output.append(root.xpath('./title/text()')[0])
    for elem in root.xpath('./text/*'):
        output.append(elem.text)
    output = ' '.join(output)

    return output

def tokenize(text, nlp) -> list:
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. 
      1. Normalize to lowercase. Strip punctuation, numbers, and `\r`, `\n`, `\t`. 
      2. Replace multiple spaces for a single space
      3. Tokenize with spacy.
      4. Remove stopwords with spacy..
      5. Remove tokens with len <= 2
      6. Apply lemmatization to words using spacy.
    """
    text = text.lower()
    text = re.sub('[' + string.punctuation + '0-9\\r\\t\\n]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    tokens = []
    doc = nlp(text)
    for token in doc:
        if not token.is_stop and len(token) > 2:
            tokens.append(token.lemma_)
    return tokens

def doc_freq(tok_corpus):
    """
    Returns a dictionary of the number of docs in which a word occurs.
    Input:
       tok_corpus: list of list of words
    Output:
       df: dictionary df[w] = # of docs containing w 
    """
    df = Counter()

    for doc in tok_corpus:
        unique_words = set(doc)
        df.update(unique_words)
    return df

def compute_tfidf_i(tok_doc: list, doc_freq: dict, N: int) -> dict:
    """ Returns a dictionary of tfidf for one document
        tf[w, doc] = counts[w, doc]/ len(doc)
        idf[w] = np.log(N/(doc_freq[w] + 1))
        tfidf[w, doc] = tf[w, doc]*idf[w]
    """
    len_doc = len(tok_doc)
    tok_freq = Counter(tok_doc)
    tfidf = {}

    for word in sorted(tok_freq.keys()):
        counts = tok_freq[word]
        tf = counts / len_doc
        idf = np.log(N/(doc_freq[word] + 1))
        tfidf[word] = tf * idf

    return tfidf

def compute_tfidf(tok_corpus:list, doc_freq: dict) -> dict:
    """Computes tfidf for a corpus of tokenized text.

    Input:
       tok_corpus: list of tokenized text
       doc_freq: dictionary of word to set of doc indeces
    Output:
       tfidf: list of dict 
               tfidf[i] is the dictionary of tfidf of word in doc i.
    """
    tfidf = []
    for doc in tok_corpus:
        tfidf.append(compute_tfidf_i(doc, doc_freq, len(tok_corpus)))
    return tfidf

def summarize(xmlfile, doc_freq, N,  n:int) -> list:
    """
    Given xml file, n and the tfidf dictionary 
    return up to n (word,score) pairs in a list. Discard any terms with
    scores < 0.01. Sort the (word,score) pairs by TFIDF score in reverse order.
    """
    nlp = spacy.load("en_core_web_sm")
    text = gettext(xmlfile)
    tok_doc = tokenize(text, nlp)

    tfidf_doc = compute_tfidf_i(tok_doc, doc_freq, N)

    tfidf_list = []
    for word, score in tfidf_doc.items():
        if score >= 0.01:
            tfidf_list.append((word, score))
    
    tfidf_list = sorted(tfidf_list, key=lambda x: x[1], reverse = True)

    return tfidf_list[:n]
