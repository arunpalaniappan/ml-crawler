import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

def inverted_indexing(contents):

    tokens = []
    
    for document in contents:
        tokens.extend(word_tokenize(document))

    tokens = list(set(tokens))

    index = {}

    for i in range(0,len(contents)):
        text = contents[i] 
        for words in tokens:
            if words in text: 
                if words not in index: 
                    index[words] = [] 
  
                if words in index: 
                    index[words].append(i+1)

    return index
