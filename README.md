# tm-domains

**Keyword_lookup.ipynb** is code for looping over previously extracted pickles to extract filtered json files

**random_sample.json** is 10,000 random articles for Jan to play with (tf-idf)

~~**travel_test_version_threshold_4.json** is a json file containing 6200 texts - half related, half unrelated to SDG1 - this is essentially a shortcut to those who want to experiment with BERT/ NN etc. It can be read straight into a dataframe: df = pd.read_json(filename)~~
THIS FILE HAS BEEN SUPPLANTED BY THE 'balanced_df_WITH_aid_with_slave_threshold_4_keep.json' FILE - EMAILED AND TO NEW FOLDER 'classify_only'

**keyword_search** contains the folder with keyword lists (5 at the moment), and the code to extract related documents (in .json) from the pickled Gigaword corpus by selecting articles containing at least *t* keywords.

~~**Gigaword_to_classifier** is our system for this task. This classification approach consists of the following steps:~~
~~1. Conversion to .json while using a basic filter (one or two words; at least one of them should be present in text or header) (this step is not included in the notebook yet!)~~
~~2. Training data part 1: ~~
~~Naïve keyword lookup: the program is provided a (hand-crafted) keyword list of terms relevant to the SDG our classifier will be trained on. If at least *t* keywords are present, the article gets the label 'related'.~~
~~3. Training data part 2: a sample of random articles is gathered from the GigaWord corpus and added to the training data.~~
~~4. The BERT-model *'bert-base-nli-mean-tokens'* is used to get the sentence embeddings(?); the model is trained. We performed a random split on the training data; our classifier (a SVM) was trained on 2/3 of the articles and tested on 1/3.~~
THIS HAS BEEN SUPERCEDED BELOW (I wish I knew how to use git properly)

**correction** Bag of Words is the Baseline system for comparison. It performed really well on the original method (i.e. pre-filter for 'poverty and 'aid ' (step 1 above) - making BERT essentially obsolete. I figured that we were clearly biased towards those two words in our test set, so I went back to square one and used Jan's lexical lookup on the entire dataset (8 million + articles - unfiltered). With *t* keywords set to 4 - it returns around 3000+ articles and the BERT system performs better.

**BOW Baseline** - takes the whole  training corpus, lower case with stop words and punctuation removed and trains. Then the test set is fit to this vector model and predictions made. 

**NEW FOLDER classify_only** This contains a .py script with supporting utils.py and an .xlsx file - assuming a user has the prepared balanced_df_WITH_aid_with_slave_threshold_4_keep.json file and balanced_df_WITH_aid_with_slave_threshold_4_keep_RoBERTa.pkl BERT embeddings pickle this will output:
- a classification report for the BERT-based system
- a classification report for the Baseline system
- a result.tsv file with columns: text,	label (gold),	predictions (BERT),	confidence,	baseline (predictions)
the confidence value is the absolute value of the distance_function array (distance to hyperplane) rounded to 3 decimal places. 

**end_to_end_classifier_test_FPC** (for public consumption) This file is an updated version of Gigaword_to_classifier. Including Neural Net and output files. 
