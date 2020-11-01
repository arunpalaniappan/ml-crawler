import re
import requests
import pandas as pd
import numpy as np
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import networkx as nx



## Functions return only the relevant weblinks
def get_relations(url):
    
    pattern = re.compile('/wiki\/([\w]+\_?)+')
    valid_url = []
    
    req = Request(url)
    html = urlopen(req)
    soup = bs(html,'lxml')
    links = []
        
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    for link in links:
        if link != None:
            if pattern.match(link):
                valid_url.append("https://en.wikipedia.org"+link)

    return valid_url

## Driver Function for collecting the inter-links
def collect_relations(urls):
    
    relations = []
    for i in range(0,len(urls)):
        relations.append(get_relations(urls[i]))

    inter_relation = []    
    for i in relations:
        inter_relation.append(list(set(i).intersection(set(urls))))

    return inter_relation


## Creating a pre-requiste DataSet for Ranking
def create_network(related_links,urls):

    N = len(urls)
    network = []

    for i in range(0,len(related_links)):
        temp = [0]*len(urls)
        for j in range(0,len(urls)):
            if urls[j] in related_links[i]:
                temp[j] = 1
        network.append(temp)
        
    G = np.array(network)
    G = nx.convert_matrix.from_numpy_matrix(G, create_using=nx.DiGraph())
    rank = nx.pagerank(G)

    
    return rank


## Driver Function to Rank Selected Webpages
def get_ranks(urls,selected_links):
    
    related_links = collect_relations(urls)

    ranks = create_network(related_links,urls)

    ranks = dict(zip(selected_links, list(ranks.values())))
    
    return ranks

        

