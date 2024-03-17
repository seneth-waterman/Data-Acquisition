from collections import defaultdict

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    # WORD(key) : DOC-IDS(value)
    index = defaultdict(set)

    # For each word w in file i, add i to the set of document IDs
    for i in range(len(files)):
        text = get_text(files[i])
        normalized_text = words(text)
        for word in normalized_text: 
            index[word].add(i)
    return index


def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    file_list = []
    for i in range(len(files)):
        counter = 0
        for term in terms: 
            if i in index[term]: 
                counter += 1
            else:
                break
        if counter == len(terms):
            file_list.append(files[i])
    return file_list
