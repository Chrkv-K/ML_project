from sklearn.metrics import recall_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn import feature_extraction, model_selection, naive_bayes, metrics, svm
import joblib
import pickle
import nltk
import re
import gensim
import logging
import urllib.request
import codecs
from gensim.models import word2vec
from sklearn.feature_extraction.text import CountVectorizer

fasttext_model = gensim.models.KeyedVectors.load('C:/Users/ekate/Desktop/Project_ML/model/214/model.model')
data = pd.read_csv('C:/Users/ekate/Desktop/Project_ML/dataset/dataset_final.csv', sep=';', decimal=';')
words_for_model = (data.drop(['tag'], axis=1))
X_train = []
for index, row in words_for_model.iterrows():
    vector = fasttext_model[row['word']]
    X_train.append(vector)
Y_train = data['tag']
C = 500.0  # = self._alpha in our algorithm
svc = svm.SVC(C=C)
#model1 = svm.SVC(kernel='linear', C=C)
#model1 = svm.LinearSVC(C=C, max_iter=10000)
#model1 = svm.SVC(kernel='rbf', gamma=0.7, C=C)
#model1 = svm.SVC(kernel='poly', degree=3, gamma='auto', C=C)

model = svc.fit(X_train, Y_train)
joblib.dump(model, "C:/Users/ekate/Desktop/Project_ML/model/my_model_svm.pkl")