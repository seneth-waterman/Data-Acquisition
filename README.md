# Data-Acquisition
This repository is a comprehensive showcase of my work in the "Data Acquisition" course, encapsulating a wide array of techniques and tools essential for effective data collection and processing.

## Assignment Overview

### Homework 1: Web Scraping Fundamentals
* **Extracting Most Used Datasets**: Developed a script to scrape and retrieve URLs for the [most viewed datasets](https://catalog.data.gov/dataset?q=&sort=views_recent+desc).
* **Leonard Cohen Song Information**: Constructed a script to collect detailed information about [Leonard Cohen’s discography](https://www.leonardcohenfiles.com/songind.html), including albums, song titles, and lyrics.
  * Album and Song Listing: Compile a unique list of Leonard Cohen’s albums and songs
  * Lyrics Retrieval: Implement functionality to input a song name and fetch its lyrics.
* **Skills**: Web scraping using Beautiful Soup, HTML parsing, and dynamic content extraction.

### Homework 2: Data Translation Pipeline
* **Objective**: Delve into data translation across CSV, XML, JSON, and HTML formats with Python, emphasizing manual CSV parsing and leveraging standard libraries for other formats.
  * `mycsv.py`: Parses CSV files into Python data structures manually.
  * `csv2html`: Converts CSV files into HTML format manually.
  * `csv2xml`: Transforms CSV files into XML format manually.
  * `csv2json`: Converts CSV files to JSON format manually.
  * `xml2csv`: Transforms XML files back into CSV format manually.
  * `json2csv`: Converts JSON files back to CSV format manually.
* **Skills**: Manual CSV parsing, HTML, XML, and JSON data generation and processing, Python scripting for data conversion tasks.

### Homework 3: TFIDF with SpaCy
* **Objective**: Utilize TFIDF analysis with SpaCy to process Reuters articles, aiming to identify keywords that effectively summarize or distinguish documents.
  * `tfidf.py`: Contains methods for processing text and computing TFIDF scores.
  * `common.py`: Identifies and displays the ten most common words from a document along with their corresponding word counts, highlighting the most frequently occurring terms.
  * `compute_tok_corpus.py`: Tokenizes the entire corpus and stores the result in a pickle file for future use.
  * `summarize.py`: Identifies the 20 words with the highest TFIDF scores per document.
* **Skills**: Advanced text processing with SpaCy, TFIDF computation and analysis, precision formatting in Python, and utilization of pickle files for efficient data handling.

### Homework 4: Search Engine Implementation
* **Objective**: Explore the efficiency gains of using hashtables over linear search through the development of a basic search engine that queries documents and displays results in a web browser.
  * This search engine accepts one or more terms, and searches a corpus for files matching *all* of those terms. 
  * `linear_search.py`: Implements basic linear search functionality for the search engine.
  * `index_search.py`: Implements a search engine using Python's built-in dict objects for indexing.
  * `htable.py`: An implementation of hashtables from scratch.
  * `myhtable_search.py`: A hashtable-based search engine developed without using dict objects, using `htable.py`.
  * `words.py`: For extracting and processing words from documents.
  * `search.py`: Executes search engine. 
* **Skills**: Mastery in implementing basic linear search algorithms, understanding and applying hashtable data structures for search efficiency, HTML generation for web display, and practical experience with Python scripting for search engine development.

### Homework 5: Recommending Articles
* **Objective**: Develop an article recommendation engine leveraging word2vec to grasp and utilize word vectors for assessing textual similarity. This includes setting up a web server to showcase and navigate through a collection of articles alongside their recommendations.
  * `doc2vec.py`: Implemented functions to read the word vector database, process the corpus of text articles, and organize data to generate article recommendations.
  * `server.py`: Flask routes were implemented to serve article recommendations.
  * `templates/articles.html` and `templates/article.html`: Utilized Jinja2 template language for dynamic HTML content generation based on article data.
* **Skills**: Proficiency in using word2vec for textual similarity analysis, constructing and utilizing word vector databases, Flask web server setup, dynamic HTML content generation with Jinja2, and practical implementation of recommendation algorithms.
