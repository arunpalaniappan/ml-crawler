from ScraperTool import wikiScraper
from Preprocessing import controller,text_cleaner
from indexing import inverted_indexing
from Querying import select_links
from Ranking import get_ranks
from FeatureCreation import create_vector
from Learning_to_rank import Model_creation
from final_ranking import ranking
from ui_form import startUI,displayUI

import re
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import numpy as np

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

    #f = open("query.txt", "r")
    
    #ui = startUI()
    Query = input("Enter your Query")
    Query = text_cleaner(Query)
    print("here")
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

        print("End of Phase 2\n")

        print("Start of phase 3\n")

        print("Learning to Rank\n")
    
        documents = []

        for i in Ranked_links:
            documents.append(cleaned_contents[i-1])

        sorted_docs, inverted_docs = create_vector(documents)
    
        train_data = list(sorted_docs)
    
        #train_data.extend(list(inverted_docs))
    
        train_pair = train_data[::-1]
    
        Y = [1]*len(sorted_docs)
    
        #Y.extend([0]*len(sorted_docs))
    
        print("After Vectorizing")

        model_results = Model_creation(np.array(train_data),np.array(train_pair),Y)
    
        print("After Modelling")
    
        final_Rank = ranking(model_results,Ranked_links)
    
        results = ""
        for i in final_Rank:
            print(urls[i],"\n")
            results += urls[i]+"\n"
            
        displayUI(results,Query)
    