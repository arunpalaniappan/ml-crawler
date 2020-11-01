import re
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs


## Functions return only the relevant weblinks
def get_wikiLinks(urls):
    
    pattern = re.compile('/wiki\/([\w]+\_?)+')
    valid_url = []
    #print("URLS",urls[1:100])
    for url in urls:
        if url != None:
            if pattern.match(url):
                valid_url.append("https://en.wikipedia.org"+url)
    return valid_url
            

## Function to get content from a Wikipedia page
def getContent(urls):

    library = []
    count = 0

    #print("Urls",len(urls))
    for url in urls:
        #print(url)
        response = requests.get(url)
        content = ""
        if response is not None:
            html = bs(response.text, 'html.parser')
            paragraphs = html.select("p")
            
            for para in paragraphs:
                content=content+para.text
                content=content+"\n"
                
        library.append(content)

    return library
    

## Function to get weblinks from a Wikipedia page
def wikiScraper(url):

    url_Q = []
    pointer = 0
    url_Q.append(url)
    
    while len(url_Q) < 100:        
        temp = url_Q[pointer]
        req = Request(temp)
        html = urlopen(req)

        soup = bs(html,'lxml')
        links = []
        
        for link in soup.findAll('a'):
            links.append(link.get('href'))

        url_Q.extend(get_wikiLinks(links))   
        pointer+=1

    #print(url_Q[:5])
    content = getContent(url_Q[:5])

    return content,url_Q


            
            
    





