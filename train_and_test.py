import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn import feature_extraction, model_selection, naive_bayes, metrics, svm
import nltk
import re
import logging
import urllib.request
from gensim.models import word2vec
from sklearn.feature_extraction.text import CountVectorizer
import gensim
import codecs

data = pd.read_csv('C:/Users/ekate/Desktop/Project_ML/dataset/dataset_final.csv', sep=';', decimal=';')
fasttext_model = gensim.models.KeyedVectors.load('C:/Users/ekate/Desktop/Project_ML/model/214/model.model')

words_for_model = (data.drop(['tag'], axis=1))
X = []
for index, row in words_for_model.iterrows():
    vector = fasttext_model[row['word']]
    X.append(vector)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, data['tag'], test_size=0.2, random_state=50)
list_C = np.arange(500, 2000, 100) #100000

score_train = np.zeros(len(list_C))
score_test = np.zeros(len(list_C))
recall_test = np.zeros(len(list_C))
precision_test= np.zeros(len(list_C))
count = 0
for C in list_C:
    svc = svm.SVC(C=C)
    svc.fit(X_train, y_train)
    score_train[count] = svc.score(X_train, y_train)
    score_test[count]= svc.score(X_test, y_test)
    recall_test[count] = metrics.recall_score(y_test, svc.predict(X_test))
    precision_test[count] = metrics.precision_score(y_test, svc.predict(X_test))
    count = count + 1

matrix = np.matrix(np.c_[list_C, score_train, score_test, recall_test, precision_test])
models = pd.DataFrame(data = matrix, columns = 
             ['C', 'Train Accuracy', 'Test Accuracy', 'Test Recall', 'Test Precision'])
print (models.head(n=10))
best_index = models['Test Precision'].idxmax()

print(models.iloc[best_index, :])
print (models[models['Test Precision']>0.90].head(5))
best_index = models[models['Test Precision']>0.90]['Test Accuracy'].idxmax()
svc = svm.SVC(C=list_C[best_index])
svc.fit(X_train, y_train)
models.iloc[best_index, :]

m_confusion_test = metrics.confusion_matrix(y_test, svc.predict(X_test))
print (pd.DataFrame(data = m_confusion_test, columns = ['Predicted 0', 'Predicted 1'],
            index = ['Actual 0', 'Actual 1']))

