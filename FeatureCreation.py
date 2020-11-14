from nltk.corpus import stopwords
from bs4 import BeautifulSoup as bs
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding
import re

 
def text_cleaner(text):
    stop_words = set(stopwords.words('english'))
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

def vectorizing(cleaned_txt):

    t = Tokenizer()
    t.fit_on_texts(cleaned_txt)
    vocab_size = len(t.word_index) + 1

    encoded_docs = t.texts_to_sequences(cleaned_txt)


    max_length = max([len(i) for i in cleaned_txt])
    padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
    paired_docs = padded_docs[::-1]

    return padded_docs,paired_docs

def create_vector(documents):

    cleaned_txt = []
    for i in range(0,len(documents)):
        cleaned_txt.append(documents[i])

    sorted_docs,inverse_sorted = vectorizing(cleaned_txt)

    return sorted_docs,inverse_sorted 
