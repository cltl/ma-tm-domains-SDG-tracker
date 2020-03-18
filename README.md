# tm-domains

**Folders:**

**Archive** contains code that's not part of any system at the moment, because it is outdated or we decided to use a different technique.

**BERT fine tuning** should be self-explanatory

**classify_only** This contains a .py script with supporting utils.py and an .xlsx file - assuming a user has the prepared balanced_df_WITH_aid_with_slave_threshold_4_keep.json file and balanced_df_WITH_aid_with_slave_threshold_4_keep_RoBERTa.pkl BERT embeddings pickle this will output:
- a classification report for the BERT-based system
- a classification report for the Baseline system
- a result.tsv file with columns: text,	label (gold),	predictions (BERT),	confidence,	baseline (predictions)
the confidence value is the absolute value of the distance_function array (distance to hyperplane) rounded to 3 decimal places.

**Corpus Extraction** contains code to extract (training) data from the Gigaword corpus we are allowed to use for this task.

**keyword_search** contains the folder with keyword lists (5 at the moment), and the code to extract related documents (in .json) from the pickled Gigaword corpus by selecting articles containing at least *t* keywords.

**Sentiment Analysis** contains the code used to train the sentiment classifier.

***Files:***

**end_to_end_classifier_test_FPC** (for public consumption) This file is an updated version of Gigaword_to_classifier. Including Neural Net and output files.
(outdated) description of the system:
1. Conversion to .json while using a basic filter (one or two words; at least one of them should be present in text or header) (this step is not included in the notebook yet!)~~
2. Training data part 1: ~~
Naïve keyword lookup: the program is provided a (hand-crafted) keyword list of terms relevant to the SDG our classifier will be trained on. If at least *t* keywords are present, the article gets the label 'related'.~~
3. Training data part 2: a sample of random articles is gathered from the GigaWord corpus and added to the training data.~~
4. The BERT-model *'bert-base-nli-mean-tokens'* is used to get the sentence embeddings(?); the model is trained. We performed a random split on the training data; our classifier (a SVM) was trained on 2/3 of the articles and tested on 1/3.

**BOW Baseline** - takes the whole  training corpus, lower case with stop words and punctuation removed and trains. Then the test set is fit to this vector model and predictions made. Bag of Words is the Baseline system for comparison. It performed really well on the original method (i.e. pre-filter for 'poverty and 'aid ' (step 1 above) - making BERT essentially obsolete. I figured that we were clearly biased towards those two words in our test set, so I went back to square one and used Jan's lexical lookup on the entire dataset (8 million + articles - unfiltered). With *t* keywords set to 4 - it returns around 3000+ articles and the BERT system performs better.

![Flow diagram of classification process](classification flow diagram.png)
