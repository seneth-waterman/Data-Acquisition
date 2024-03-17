from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    table = htable(4011)

    for i in range(len(files)):
        text = get_text(files[i])
        normalized_text = words(text)
        for word in normalized_text:
            bucket_index = bucket_indexof(table, word)
            if len(table[bucket_index]) > 0:
                bucket_keys = [item[0] for item in table[bucket_index]]
            else:
                bucket_keys= []

            if word not in bucket_keys:
                table[bucket_index].append((word, {i}))
            elif word in bucket_keys:
                for elem in table[bucket_index]:
                    if elem[0] == word:
                        elem[1].add(i)
    return table


def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    file_list = []
    for i in range(len(files)):
        counter = 0
        for w in terms: 
            if htable_get(index, w) is not None and i in htable_get(index, w): 
                counter += 1
            else:
                break
        if counter == len(terms):
            file_list.append(files[i])
    return file_list
