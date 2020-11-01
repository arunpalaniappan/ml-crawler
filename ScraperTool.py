import re
import requests
from urllib.request import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup as bs
import random
import numpy as np

from Preprocessing import text_cleaner

#Utility: Collects wiki pages from the internet, scraps text and stores them in a dataframe.

## Function to get content from a Wikipedia page
def getContent(url):
    """
    Given a wiki url, the function gets the content in the page
    and returns them as a dictionary of type {'url':url, 'raw_content':content}
    """
    response = requests.get(url)
    content = ""
    if response is not None:
        html = bs(response.text, 'html.parser')
        paragraphs = html.select("p")
            
        for para in paragraphs:
            content=content+para.text
            content=content+"\n"
    return content
    

## Function to get weblinks from a Wikipedia page
def getLinks(url):
    """
    Given the source url, the function gets wiki urls from the page
    """
    print (url)
    req = Request(url)
    html = urlopen(req)
    soup = bs(html,'lxml')

    pattern = re.compile('/wiki\/([\w]+\_?)+')
    
    links = []
        
    for link in soup.findAll('a'):
        links.append(link.get('href'))

        
    valid_url = []
    
    for link in links:
        if link and pattern.match(link) and (":" not in link):
            #Some links are like 'https://en.wikipedia.org/wiki/Category:Computer_science', 'https://en.wikipedia.org/wiki/Special:MyContributions'
            #It would be better if we could integrate this in pattern match
            link = "https://en.wikipedia.org"+link
            if link not in valid_url:
                valid_url.append(link)

    return valid_url


def wikiScraper(n=100):
    """

    This function is used to index documents in the web.
    
    n - number of documents to be indexed
    
    """
    urls = df.read_csv("Data\\urls.csv")
    """
    We will be indexing documents (links) in the urls file.

    Relavant indexing technique has to be studies
    """
    
    return (df)


def makeDatabase(start_url="https://en.wikipedia.org/wiki/Machine_learning", n=2000):
    """
    Creates the database (finds links) which will serves as collection of documents.
    n - number of documents
    """
    urls = [start_url]
    while len(urls) < n:
        url = random.sample(urls, 1)[0]
        urls.extend(getLinks(url))
        urls = list(set(urls))

    df = pd.DataFrame({'urls':urls, 'url_index':np.arange(0, len(urls), 1)})
    df.to_csv('Data\\urls.csv', index=False)
    return df
