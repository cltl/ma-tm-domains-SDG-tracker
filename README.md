# SDG-tracker
This repository contains a student project for the MA Text Mining course Text Mining Domains.
2020, Vrije Universiteit, Amsterdam.

**The UN Sustainable Development Goals**

Companies are increasingly tasked with acting in a socially responsible manner; how a company is perceived can affect its brand image and consequently, its value. Actively contributing towards goals which benefit society and communities is a way in which a company can distinguish itself from its competitors and enhance how brands are perceived by existing and potential customers. Conversely, actions which negatively impact  communities or are perceived to sacrifice long term sustainability for short term goals can pose a risk to a company’s image and the prestige of their brands.

One overarching measure of global performance towards a better, more sustainable society is described by the UN’s <a href="https://www.un.org/sustainabledevelopment/sustainable-development-goals">Sustainable Development Goals (SDGs)</a>. The SDGs set in 2015 by the United Nations General Assembly are a collection of global goals intended to be achieved by the year 2030 and designed to be a "blueprint to achieve a better and more sustainable future for all" (dpicampaigns, 2019).

Companies have acted to incorporate SDG outcomes in their company policy, however, it is insufficient to merely encode these goals in policy documents, and these goals have to be somehow translated into actions and behaviours throughout the company. In large scale corporations, this can be difficult to translate into company culture, and difficult to monitor, especially when subsidiaries and supply chains are taken into account. 

From a business consultancy perspective, monitoring performance on how a company is translating policy into actions is crucial to be able to predict future company performance, yet monitoring large complex multinational organisations is no trivial task, especially around qualitative aims 

One way of monitoring how a company is performing is to monitor public perception directly for evidence of actions that relate to these goals. 

**SDG-tracker**

SDG-tracker is an effort to assist in the verification of companies' compliance to the UN’s Sustainable Development Goals (SDGs), using Machine Learning. We have developed an application that classifies news articles on their relation to one of the Sustainable Development Goals.
For this task, we use a BERT-based machine learning approach to determine whether a news article is relevant to one of the SDGs. The training data was created by a lexical lookup on a vast corpus (GigaWord).

The file **end_to_end_classifier.ipynb** shows the process of creating the training set, the training of the SDG-classifier and the classifier's application on unseen news articles we have extracted manually (the test sets for SDG1 (end all poverty) and SDG12 (sustainable consumption).
Manually created keyword lists are provided for several SDGs, although some of these are short (see <a href="/keyword_search/keywords"> keyword_search/keywords</a>.
In the folder Sentiment_Analysis, our sentiment classification approach is shown. The idea is to filter whether an article states something positive about a company with regard to one of the SDGs.

**Folders**

**Corpus Extraction** contains code to extract (training) data from the Gigaword corpus we are allowed to use for this task.

**Pretrained classifiers related-unrelated** contains pretrained classifiers for SDGs 1 and 12.

**classify_only** This contains a .py script with supporting utils.py and an .xlsx file - assuming a user has the prepared:
- balanced_df_WITH_aid_with_slave_threshold_4_keep.json file, and 
- balanced_df_WITH_aid_with_slave_threshold_4_keep_RoBERTa.pkl BERT embeddings pickle 

This will output:
- a classification report for the BERT-based system
- a classification report for the Baseline system
- a result.tsv file with columns: text,	label (gold),	predictions (BERT),	confidence,	baseline (predictions)
the confidence value is the absolute value of the distance_function array (distance to hyperplane) rounded to 3 decimal places.

**keyword_search** contains the folder with keyword lists (5 at the moment), and the code to extract related documents (in .json) from the pickled Gigaword corpus by selecting articles containing at least *t* keywords. There is an option to extract TF-IDF scores for the keywords in the document, but this feature was not used for the final system because an inspection of the results did not show a contribution to the task (docs with low TF-IDF scores for their keywords were generally not less related to the SDG than their counterparts obtaining a higher score).

**Sentiment Analysis** contains the code used to train the sentiment classifiers, and the pretrained sentiment classifiers.

***Files:***

**Legals report Text Mining Domains** is the full application report, containing a description of the system, error analysis and recommendations for futher development.

**end_to_end_classifier_test_FPC** 

Description of the system. 
There are two potential ways to use it - with the full GigaWord corpus, or with copies of files which have been filtered. 

1. The first part of the workflow assumes you have the full GigaWord corpus as a json file (frame_to_rule2.json). This was iteratively constructed by filtering <a href="https://catalog.ldc.upenn.edu/LDC2003T05">the Gigaword corpus</a> and extracting the headlines and first five sentences in several stages. The first step is to load the entire dataframe into memory (memory intensive but allows the filtering section to be performed quickly).

2. Training data part 1: 
Naïve keyword lookup: the program is provided a manually created keyword list of terms relevant to the SDG our classifier will be trained on. If at least *t* keywords are present, the article gets the label 'related'. Duplicate texts are dropped at. (in the system as it now stands, *t* is set to 4. 

3. Training data part 2: 
a sample of random articles is gathered from the GigaWord corpus and added to the training data. 
- The fastest way to do this is to simply sample fromt he full Gigaword corpus and then prune duplicates. However every time I attempt this, the classifier drops 10 points. I cannot explain why. 
- The far slower way to do this (but more effective) is to iterate over fragments of the GigaWord corpus and pull a random news story. This is first done at 110%  the length of the results of step 2, above. Duplicates are then dropped, these are labelled 'unrelated'.

The related and unrelated dataframes are concatenated and pruned to the final length to produce a 50:50 related : unrelated training set.

*BOW Baseline*
- takes the whole training corpus, lowers the case and removes stop words and punctuation before training. The test set is fit to this vector model and predictions are made. Bag of Words is the Baseline system for comparison.

4. The BERT-model *'roberta-large-nli-mean-tokens'* is used to get the sentence embeddings which are subsequently concatenated to get a single vector representation for each text in the training set. This method is also used to encode the sentences in the test set. 

These are used for two classification methods with the results compared. 
- SVM
- MLP (NN)

5. Output:
- there is a classification report printed to screen for each classifier. 
- the last cell produces a tsv file containing columns for:
   (each) 'text', (gold) 'label', 'SVM_predictions', 'SVM_confidence'(distance to hyperplane), 'NN_predictions', 'NN_confidence' (probability), 'Baseline_predictions'


Flow diagram of the classification process:
<div align="center">
    <img src="images/classification flow diagram.png" width="800px"</img> 
</div>

**Acknowledgement**

This project was created as part of the course Text Mining Domains, offered by CLTL at Vrije Universiteit, Amsterdam.

**Authors**

Adam Tucker

Jan van Casteren

Merel de Groot

Michiel van Nederpelt

Peter Caine

Supervisor: prof. dr. P.T.J.M. Vossen.

Computational Lexicology & Terminology Lab, Vrije Universiteit Amsterdam.
