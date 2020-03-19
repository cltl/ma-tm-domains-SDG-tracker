# tm-domains

**Folders:**

**Archive** contains code that's not part of any system at the moment, because it is outdated or we decided to use a different technique.

**BERT fine tuning** should be self-explanatory

**classify_only** This contains a .py script with supporting utils.py and an .xlsx file - assuming a user has the prepared:
- balanced_df_WITH_aid_with_slave_threshold_4_keep.json file, and 
- balanced_df_WITH_aid_with_slave_threshold_4_keep_RoBERTa.pkl BERT embeddings pickle 

this will output:
- a classification report for the BERT-based system
- a classification report for the Baseline system
- a result.tsv file with columns: text,	label (gold),	predictions (BERT),	confidence,	baseline (predictions)
the confidence value is the absolute value of the distance_function array (distance to hyperplane) rounded to 3 decimal places.

**Corpus Extraction** contains code to extract (training) data from the Gigaword corpus we are allowed to use for this task.

**keyword_search** contains the folder with keyword lists (5 at the moment), and the code to extract related documents (in .json) from the pickled Gigaword corpus by selecting articles containing at least *t* keywords.

**Sentiment Analysis** contains the code used to train the sentiment classifier.

***Files:***

**end_to_end_classifier_test_FPC** (for public consumption) This file is an updated version of Gigaword_to_classifier. Including Neural Net and output files.

Description of the system. 
There are two potential ways to use it - with the full GigaWord corpus, or with copies of files which have been filtered. 

1. The first part of the workflow assumes you have the full GigaWord corpus as a json file (frame_to_rule2.json). This was iteratively constructed by filtering the Gigaword corpus and extracting the headlines and first five sentences in several stages. Ask Peter or Jan for a copy (7GB+). The first step is to load the entire dataframe into memory (memory intensive but allows the filtering section to be performed quickly)

2. Training data part 1: 
Naïve keyword lookup: the program is provided a (hand-crafted) keyword list of terms relevant to the SDG our classifier will be trained on. If at least *t* keywords are present, the article gets the label 'related'. Duplicate texts are dropped at. (in the system as it now stands, *t* is set to 4. 

3. Training data part 2: 
a sample of random articles is gathered from the GigaWord corpus and added to the training data. 
- The fastest way to do this is to simply sample fromt he full Gigaword corpus and then prune duplicates. However every time I attempt this, the classifier drops 10 points. I cannot explain why. 
- The far slower way to do this (but more effective) is to iterate over fragments of the GigaWord corpus and pull a random news story. This is first done at 110%  the length of the results of step 2, above. Duplicates are then dropped, these are labelled 'unrelated'.

The related and unrelated dataframes are concatenated and pruned to the final length to produce a 50:50 related : unrelated training set.

**BOW Baseline** - takes the whole training corpus, lowers the case and removes stop words and punctuation before training. The test set is fit to this vector model and predictions are made. Bag of Words is the Baseline system for comparison.

4. The BERT-model *'roberta-large-nli-mean-tokens'* is used to get the sentence embeddings which are subsequently concatenated to get a single vector representation for each text in the training set. This method is also used to encode the sentences in the test set. 

These are used for two classification methods with the results compared. 
- SVM
- MLP (NN)


Flow diagram of the classification process:
<div align="center">
    <img src="images/classification flow diagram.png" width="800px"</img> 
</div>
