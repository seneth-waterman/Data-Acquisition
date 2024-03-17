import os
import re
import string


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    all_items = os.listdir(root)
    files = []
    for item in all_items:
        abs_path_item = f'{root}/{item}'
        if os.path.isfile(abs_path_item):
            print(abs_path_item)
            files.append(abs_path_item)
        elif os.path.isdir(abs_path_item):
            dir_items = os.listdir(abs_path_item)
            for subfile in dir_items:
                abs_path_subitem = f'{abs_path_item}/{subfile}'
                if os.path.isfile(abs_path_subitem):
                    files.append(abs_path_subitem)             
    return files


def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    html = f'<html>\n    <body>\n       <h2>Search results for <b> {terms[0]}</b> in {len(docs)} files</h2>\n'
    for doc in docs[:100]: 
        matches = " "
        with open(doc, "r") as file:
            for line in file: 
                match = re.match(f'.*{terms[0]}.*', line.lower())
                if match is not None: 
                    matches = line.strip('\n').strip()
                    break
        html += f'       <p> <a href=file://{doc}</a><br>\n'   
        html += f'       {matches}<br><br>\n'
    html += '</body>\n</html>'
    return html


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]
