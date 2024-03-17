from tfidf import *
from collections import Counter
import sys

"""
Print the most common 10 words from a documents and the word count.

1. Use gettext to get the text of the xml file.
2. Tokenize the text with tokenize.
3. Compute word counts with Counter.
4. Print most common words with counts.
"""

path = sys.argv[1]
text = gettext(path)
nlp = spacy.load("en_core_web_sm")
tokens = tokenize(text, nlp) 
wc = Counter(tokens)
for elem in wc.most_common(10):
    print(elem[0], elem[1])
