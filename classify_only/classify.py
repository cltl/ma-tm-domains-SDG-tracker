import pickle
import numpy as np
import pandas as pd
from nltk.corpus import stopwords

from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

from utils import BERT_encode_sentences, prep_baseline
from sklearn.feature_extraction.text import CountVectorizer

# default paths to existing files
articles_path = './saved_models/balanced_df_WITH_aid_with_slave_threshold_4_keep.json'
embeddings_path = './saved_models/balanced_df_WITH_aid_with_slave_threshold_4_keep_RoBERTa.pkl'

# ask user for input
training_data = input("Do you have pre-selected balanced dataset? Y/N ")
training_data = training_data.lower()
prepared_embeddings = input("Do you have pre-trained embeddings? Y/N ")
prepared_embeddings = prepared_embeddings.lower()

if training_data == 'y':
    training_data_path = input("enter path to training dataset: ")
    if training_data_path == '':
        training_data_path = articles_path
    balanced_labeled_df = pd.read_json(training_data_path, encoding='utf-8')
else:
    pass

texts = balanced_labeled_df.text.to_list()

if prepared_embeddings == 'y':
    embeddings_data_path = input("enter path to embeddings file: ")
    if embeddings_data_path == '':
        embeddings_data_path = embeddings_path
    # load prepared sentence_embeddings
    # # these are concatenated transformers trained on RoBERTa
    concatenated_train_X = pickle.load(open(embeddings_data_path, 'rb'))
else:
    # mod = input('enter 0 for RoBERTa model or 1 for BERT nli')
    concatenated_train_X, mean_train_X = BERT_encode_sentences(texts)

train_y = list(balanced_labeled_df.label)

################# assemble test data ###########################
# excel sheet name 'Related_SDG1' is both costa and starbucks aggregated data
df = pd.read_excel('combined_testset.xlsx', sheet_name='Related_SDG1')
# headline and first 5 sentences are in two separate columns
df['text'] = df['Headline'].astype(str)+' '+df['First 5 sentences']
df = df[['text', 'label']]
test_texts = df['text'].to_list()

concatenated_test_X, mean_test_X = BERT_encode_sentences(test_texts)
test_y = df['label'].to_list()

######################### BERT Classifier ################################
BERT_clf = LinearSVC(random_state=0, tol=1e-5, max_iter=5000)
# can change concatenated to mean but concatenated seems to offer slight improvements
BERT_clf.fit(concatenated_train_X, train_y)

predictions = list(BERT_clf.predict(concatenated_test_X))
print('RoBERTa results:', '\n', classification_report(test_y, predictions))

df['predictions'] = predictions
confidence = BERT_clf.decision_function(concatenated_test_X)
df['confidence'] = np.round(abs(confidence), 3).tolist()

######################## Baseline Classifier ###########################
concatenated_sents = prep_baseline(texts)

big_count_vec = CountVectorizer(stop_words=stopwords.words('english'))
BOW_model = big_count_vec.fit_transform(concatenated_sents)
BOW_test_X = big_count_vec.transform(test_texts)
BOW_train_y = train_y
BOW_test_y = test_y
BOW_clf = LinearSVC(random_state=0, tol=1e-5)
BOW_clf.fit(BOW_model, BOW_train_y)

predicted_label = BOW_clf.predict(BOW_test_X)
print('Baseline results:', '\n', classification_report(BOW_test_y, predicted_label))

df['baseline'] = predicted_label

# write the results to file
df.to_csv('results.tsv', sep='\t')
