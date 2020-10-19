from nltk.corpus import stopwords
from bs4 import BeautifulSoup as bs
import re

stop_words = set(stopwords.words('english')) 

def text_cleaner(text):
 
    cleanedText = text.lower()
    cleanedText = bs(cleanedText, "lxml").text
    cleanedText = re.sub(r'\([^)]*\)', '', cleanedText)
    cleanedText = re.sub('"','', cleanedText)
    cleanedText = re.sub(r"'s\b","",cleanedText)
    cleanedText = re.sub("[^a-zA-Z]", " ", cleanedText) 
    tokens = [w for w in cleanedText.split() if not w in stop_words]
    
    long_words=[]

    for i in tokens:
        long_words.append(i)   

    return (" ".join(long_words)).strip()
