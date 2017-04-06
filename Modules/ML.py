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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import  linear_model
import sklearn

import scipy
from sklearn import metrics
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline

def modelToFile(model, name="Noname", path=os.getcwd()):
    path_f = path + "\\"
    if not os.path.exists(path_f+name):
        os.mkdir(path_f+name)
    path_f = path_f + name
    joblib.dump(model, str(path_f)+"\\"+name+".mdl")
    return path_f

def modelFromFile(name="Noname", path=os.getcwd()):
    load_model = joblib.load(str(path)+"\\"+name + ".mdl")
    return load_model


csv.field_size_limit(sys.maxsize)
plt.interactive(False)
path_f = 'k:/Andrew/vkr/example/f40k_csv_ravn_NA/'
path_model = 'K:\\Andrew\\Programming\\VKR\\Results'

list_f = os.listdir(path_f)
data = pd.DataFrame()
for el in list_f[:3]:
    df = pd.read_csv(path_f+el, encoding='utf-8', usecols=['0','1','2'], nrows=100)
    data = data.append(df, ignore_index=True)
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
print(len(train_data))
# clf_text = Pipeline([
#     ('cntvec' ,CountVectorizer(analyzer='word', tokenizer=nltk.word_tokenize)),
#     ('logreg', linear_model.LogisticRegression(n_jobs=1, C=1e5)),
#     ])

cntvec = CountVectorizer(analyzer='word', tokenizer=nltk.word_tokenize)
train_data_features = cntvec.fit_transform(train_data['2'])

logreg = linear_model.LogisticRegression(n_jobs=1, C=1e5)
logreg = logreg.fit(train_data_features, train_data['0'])
#print(len(cntvec.get_feature_names()))
#print(train_data[train_data['2'].str.contains("ятельнейший")==True])

test_data_features = cntvec.transform(test_data['2'])
predicted = logreg.predict(test_data_features)
print(np.mean(predicted == test_data['0']))


# clf_text = clf_text.fit(train_data['2'], train_data['0'])
#
# path_mdl = modelToFile(clf_text, "Probe", path_model)
# clf_text = modelFromFile("Probe", path_mdl)
#
# predicted =  clf_text.predict(test_data['2'])
# print(np.mean(predicted == test_data['0']))