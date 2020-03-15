# tm-domains

**Keyword_lookup.ipynb** is code for looping over previously extracted pickles to extract filtered json files

**random_sample.json** is 10,000 random articles for Jan to play with (tf-idf)

**travel_test_version_threshold_4.json** is a json file containing ~6200 texts - half related, half unrelated to SDG1 - this is essentially a shortcut to those who want to experiment with BERT/ NN etc. It can be read straight into a dataframe: df = pd.read_json(filename)
THIS FILE WAS UPDATED TO REMOVE DUPLICATES 

**keyword_search** contains the folder with keyword lists (5 at the moment), and the code to extract related documents (in .json) from the pickled Gigaword corpus.

**Gigaword_to_classifier** is our *baseline system* for this task. This classification approach consists of the following steps:
1. Conversion to .json while using a basic filter (one or two words; at least one of them should be present in text or header) (this step is not included in the notebook yet!)
2. Training data part 1: 
Naïve keyword lookup: the program is provided a (hand-crafted) keyword list of terms relevant to the SDG our classifier will be trained on. If at least *t* keywords are present, the article gets the label 'related'.
3. Training data part 2: a sample of random articles is gathered from the GigaWord corpus and added to the training data.
4. The BERT-model *'bert-base-nli-mean-tokens'* is used to get the sentence embeddings(?); the model is trained. We performed a random split on the training data; our classifier (a SVM) was trained on 2/3rd of the articles and tested on 1/3rd.
