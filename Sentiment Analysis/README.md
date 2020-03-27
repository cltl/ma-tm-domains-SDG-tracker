Sentiment Analysis

*Training Data*

**Sentiment analysis training set for classifier.py** 

For the training of our sentiment classifier we made use of the MPQA data-set.
Only the files containing annotated sentiment (.feat) were used and the explainatory .log files were discarded.
.feat files were first transformed to .CSV files to make use of the 
CSV module and ConuLL module for sentiment feature extraction. After extraction sentences were scored on 
being negative, neutral or positive with a sum method giving one value (and thus a label) per sentence to be put 
in the classifier. Further improvement of the classifier could be obtained by first scoring the sentence without 
attributing a label per sentence but instead use a score, which could "help" the classifier determine sentiment further.

**docsentclassifier-RoBERTa.ipynb**

**docsentclassifier.ipynb**

**The pretrained classifiers:**
sentimentMLPsgd.pkl
sentimentNB.pkl
sentimentSVM.pkl
