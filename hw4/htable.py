"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    buckets = [[] for i in range(nbuckets)]
    return buckets


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if type(o) == str:
        h = 0
        for c in o: 
            h = h*31 + ord(c)
    elif type(o) == int:
        h = o 
    else:
        h = None
    return h


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    bucket_index = hashcode(key) % len(table)
    return bucket_index


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """
    bucket_index = bucket_indexof(table, key)

    if len(table[bucket_index]) > 0:
        bucket_keys = [item[0] for item in table[bucket_index]]
    else:
        bucket_keys = []

    if key not in bucket_keys:
        table[bucket_index].append((key, value))
    elif key in bucket_keys:
        for elem in table[bucket_index]:
            if elem[0] == key:
                table[bucket_index].remove(elem)
                table[bucket_index].append((key, value))


def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    bucket_index = bucket_indexof(table, key)
    for elem in table[bucket_index]:
        if elem[0] == key:
            return elem[1]


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    string = ""
    for i in range(len(table)):
        if len(table[i]) == 0:
            string += f"{i:04}->\n"
        else:
            string += f"{i:04}->"
            for elem in table[i]:
                string += f"{elem[0]}:{elem[1]}, "
            string = string[:-2] + "\n"
    return string
    

def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    dic_str = "{"
    for elem in table:
        if len(elem) > 0:
            for item in elem:
                dic_str += f"{item[0]}:{item[1]}, "
    if len(dic_str) > 1:
        dic_str = dic_str[:-2]
    dic_str += "}"
    return dic_str
