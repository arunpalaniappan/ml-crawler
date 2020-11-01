from ScraperTool import wikiScraper
from indexing import inverted_indexing

import re
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

##import nltk
##from nltk.corpus import stopwords
##from nltk.tokenize import word_tokenize 
##nltk.download('stopwords') 

import re
import operator

import pandas as pd

if __name__ == '__main__':

    print("Welcome:")

    #The below line is to be uncommented to collect data and pre-process data,
    #otherwise to use existing data, not required to modify code
    
    df = wikiScraper()
    #df = pd.read_csv('Documents\\raw_data.csv')
    
##    print("Before Preprocessing",contents[0])
##    
##    cleaned_contents = controller(contents)
##
##    print("After Preprocessing",cleaned_contents[0])

##    inverted_index = inverted_indexing(cleaned_contents)
##
##    print("After indexing")
##
##    for k,v in sorted(inverted_index.items(), key=operator.itemgetter(1))[1000:1100]:
##        print (k,v)
##
##    print("End of Phase 1")
