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
from sklearn.externals import joblib


def modelFromFile(name="Noname", path=os.getcwd()):
    name = name + ".mdl"
    load_model = joblib.load(str(path)+"\\"+name)
    return load_model
path_f = 'k:/Andrew/vkr/example/f40k_csv_ravn_NA/'
list_f = os.listdir(path_f)
data = pd.DataFrame()
for el in list_f[:3]:
    df = pd.read_csv(path_f+el, encoding='utf-8', usecols=['0','1','2'], nrows=100)
    data = data.append(df, ignore_index=True)


clf = modelFromFile(name="Probe", path="K:\Andrew\Programming\VKR\Results")
predicted = clf.predict(data['2'])
print(np.mean(predicted == data['0']))





