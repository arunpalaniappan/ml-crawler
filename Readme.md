# ML Querier

**Data:** Scrapping of wikipedia pages

## Abstract:
In this project, we aim to build an information retrieval system for queries related to machine learning terminologies. Data is collected by scrapping wikipedia pages which are related to machine learning ex: entropy, data science, natural language processing. We will start a web crawler from the root page which we are setting as https://en.wikipedia.org/wiki/Machine_learning. From here, the crawler follows a breadth first search toe th links in the pages (ex: data science, natural language processing, entropy, gini) and irrelevant links are weeded out. Such a crawling will result in a collection of documents. The next step is pre-processing of the texts and using the pre-processed text in the collected documents, we aim to build an information retrieval system which retrieves the relevant documents for a given query. We choose a suitable document representation system and to retrieve them, document similarity metrics will be used. The retrieved documents will be ranked based on ranking metrics and we aim to use bandit algorithms for improving on ranking based on user click feedback.


## File Description

**__main__.py**

 	* driver file which should be read in order to execute the package

**ScraperTool.py**

	* wikiScraper() - collects documents from web

	* getLinks() - Get valid links from page given url

	* getContent() - Gets content from wikipedia page given page url

**Preprocessing.py**

	* text_cleaner() - Preprocessing the text

**indexing.py**

	* inverted_indexing() - generates inverted index of the documents
	


**Ranking.py**

	* get_ranks() - Driver Function to Rank Selected Webpages

	* get_relations() - Functions return only the relevant weblinks

	* collect_relations()- Driver Function for collecting the inter-links
	
	* create_network() - Creating a pre-requiste DataSet for Ranking


**Querying.py**

	* select_links() - Selecting Links based on the Query



**FeatureCreation.py**

	* text_cleaner() - cleaning the dataset
	
	* vectorizing() - Converting the data into vector form
	
	* create_vector() - driver functions 
	

**Learning_to_rank.py**

	* RankNet() - Architecture of the RankNet

	* Model_creation() - Driver function to train and text
	

**final_Ranking.py**

	* Ranking() - Final ranking based on Train and Test


**ui_form.py**

	* displayUI() -Function to display the UI
