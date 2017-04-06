import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
import pandas as pd
import csv
import codecs
import numpy as np
import string
import sys
import matplotlib.pyplot as plt
import os
import tqdm
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import  linear_model

import scipy

csv.field_size_limit(sys.maxsize)
plt.interactive(False)
path_f = 'k:/Andrew/vkr/example/f40k_csv_ravn_NA/'

list_f = os.listdir(path_f)
data = pd.DataFrame()
for el in list_f[:5]:
    df = pd.read_csv(path_f+el, encoding='utf-8', usecols=['0','1','2'])
    data = data.append(df, ignore_index=True)
train_data, test_data = train_test_split(data, test_size=0.1, random_state=42)
print(len(train_data))
tokens = nltk.word_tokenize(train_data.iat[0,2])
cntvec = CountVectorizer(analyzer='word', tokenizer=nltk.word_tokenize)
train_data_features = cntvec.fit_transform(train_data['2'])

logreg = linear_model.LogisticRegression(n_jobs=1, C=1e5)
logreg = logreg.fit(train_data_features, train_data['0'])
print(len(cntvec.get_feature_names()))
#print(train_data[train_data['2'].str.contains("ятельнейший")==True])
