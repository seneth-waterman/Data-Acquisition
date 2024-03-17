# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    output = []
    # Look at each file
    for file in files:
        # normalize the file with words()
        text = get_text(file)
        normalized_text = words(text)

        counter_list = terms.copy()
        # Are all of the terms (string list) in this file? 
        for word in normalized_text:
            if word in terms and word in counter_list:
                # remove word from list
                counter_list.remove(word)
        # yes - add to output 
        if len(counter_list) == 0:
            output.append(file)

    return output
