import re
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

from Preprocessing import text_cleaner

import pandas as pd

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
    req = Request(url)
    html = urlopen(req)
    soup = bs(html,'lxml')

    pattern = re.compile('/wiki\/([\w]+\_?)+')
    
    links = []
        
    for link in soup.findAll('a'):
        links.append(link.get('href'))

        
    valid_url = []
    
    for link in links:
        if link and pattern.match(link) and ":" not in link:
            #Some links are like 'https://en.wikipedia.org/wiki/Category:Computer_science', 'https://en.wikipedia.org/wiki/Special:MyContributions'
            #It would be better if we could integrate this in pattern match
            valid_url.append("https://en.wikipedia.org"+link)

    return valid_url


def wikiScraper(start_url="https://en.wikipedia.org/wiki/Machine_learning", n=100):
    """
    n - number of documents
    """
    url_Q = []
    pointer = 0

    urls = []
    contents = []

    url = start_url
    for i in range(n): 
        urls.append(url)
        contents.append(getContent(url))
        url_Q.extend(getLinks(url))
        url = url_Q[i]

    df = pd.DataFrame({'url':urls, 'content':contents})
    df['content'] = df['content'].apply(text_cleaner)    
    df.to_csv('Documents\\raw_data.csv', index=False)

    return (df)

