import os
import random
import glob
import json
import nltk
import re
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer

from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


def BERT_encode_sentences(texts, mod=0):
    '''
    takes a list of texts and name of model as input (default model = Bert_large)
    returns a list of concatenated BERT embeddings and a list of mean (averaged)
    BERT embeddings for input as X in a classifier

    '''
    if mod == 0:
        model = SentenceTransformer('roberta-large-nli-mean-tokens')
    else:
        model = SentenceTransformer('bert-large-nli-mean-tokens')

    embedded_texts = []
    for text in texts:
        sentences = nltk.sent_tokenize(text)
        if len(sentences) >= 6:
            sentence_embeddings = model.encode(sentences[:6])
        else:
            for n in range(6-len(sentences)):
                sentences.append(sentences[0])
                sentence_embeddings = model.encode(sentences[:6])
        embedded_texts.append(sentence_embeddings)

    concatenated_X = []
    mean_X = []

    for six_embeds in embedded_texts:
        new = np.concatenate(six_embeds)
        concatenated_X.append(new)
        mean_embeds_per_text = np.mean(six_embeds, axis=0)
        mean_X.append(mean_embeds_per_text)

    return concatenated_X, mean_X


def prep_baseline(texts):
    '''
        takes a list of texts and creates a Bag of Words ready model with
        lower case characters and punctuation/ symbols removed
    '''

    # cleaning the texts for lower case words only
    BOW_texts_list = []

    for text in texts:
        sentences = nltk.sent_tokenize(text)

        new_text = []
        if len(sentences) >= 6:
            for sent in sentences[:6]:
                # corpus.append(sent)
                sent = sent.lower()
                sent = re.sub(r'\W', ' ', sent)
                sent = re.sub(r'\s+', ' ', sent)
                new_text.append(sent)
                # processed_corpus.append(sent)

        else:
            for sent in sentences:
                # corpus.append(sent)
                sent = sent.lower()
                sent = re.sub(r'\W', ' ', sent)
                sent = re.sub(r'\s+', ' ', sent)
                new_text.append(sent)
                # processed_corpus.append(sent)
        BOW_texts_list.append(new_text)

    # each text is a single string after this
    concatenated_sents = [''.join(item)for item in BOW_texts_list]
    return concatenated_sents
