import sys

def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()

def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    data = data.split('\n')
    headers = data[0].split(',')

    new_data = []
    for i in range(1, len(data)):
        row = data[i].split(',')
        new_data.append(row)

    data = new_data

    return headers, data
