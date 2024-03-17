import sys
from bs4 import BeautifulSoup
import requests


# feel free to define other functions

def list_of_pairs(n):
    """ Get first n datasets

    Output: list of (dataset title, url)
    """
    list = []
    page = 1
    counter = 0

    while counter < n: 
        DataURL = f"https://catalog.data.gov/dataset/?q=&sort=views_recent+desc&page={page}"
        response = requests.get(DataURL)
        soup = BeautifulSoup(response.text, "lxml")
        sections = soup.find_all('h3')
        for i in range(len(sections)):
            if counter < n:
                list.append((sections[i].find('a').text, 'https://catalog.data.gov' + sections[i].find('a')['href'],))
                counter += 1
            else: 
                break
        page += 1
    
    return list

if __name__ == "__main__":
    n = int(sys.argv[1])
    pairs = list_of_pairs(n)
    for title, url in pairs:
        print(title, url)

