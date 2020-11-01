from ScraperTool import wikiScraper
from Preprocessing import controller,text_cleaner
from indexing import inverted_indexing
from Querying import select_links
from Ranking import get_ranks

import re
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
nltk.download('stopwords') 

import re
import operator

if __name__ == '__main__':

    print("Welcome:")
    
    contents, urls = wikiScraper("https://en.wikipedia.org/wiki/Machine_learning")

    print("Before Preprocessing",contents[0])
    
    cleaned_contents = controller(contents)

    print("After Preprocessing",cleaned_contents[0])

    inverted_index = inverted_indexing(cleaned_contents)

    print("After indexing")

    for k,v in sorted(inverted_index.items(), key=operator.itemgetter(1))[1000:1100]:
        print (k,v)

    print("End of Phase 1")


    print("Before Querying")

    Query = str(input("Enter the Query"))

    Query = text_cleaner(Query)
    
    selected_links = select_links(inverted_index, Query)

   
    
    print("After Querying")
    print('\n')
    print("Before Ranking")

    if selected_links == set():
        print("No Matching Found")

    else:

        links = [urls[i] for i in selected_links]
        
        Ranked_links = get_ranks(links,selected_links)
        Ranked_links = sorted(Ranked_links, key=Ranked_links.get,reverse=True)

        print("Search Results\n")

        for i in Ranked_links:
            print(urls[i],"\n")
        
    print("After Ranking\n")

    print("End of Phase 2")
    
