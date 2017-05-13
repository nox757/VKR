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






def ploting():
    plt.interactive(False)
    path_f = 'k:/Andrew/vkr/example/f40k2/'
    list_c = os.listdir(path_f)
    mystat = []
    for cat in list_c:
        mystat.append((int(cat),len(os.listdir(path_f+cat))))
    print(mystat)
    df = pd.DataFrame(data=mystat, columns=['0', '1'])
    df = df.sort(['1'], ascending=False)[:51]

    print(df.head())
    plt.figure(figsize=(20,5)).suptitle("Количество по категориям")
    plt.xlabel("Категории")
    plt.ylabel("Количество статей")
    df['1'].plot(kind='bar',rot=0).set_xticklabels(df['0'])

    plt.show()

def count_cat():
    path_f = 'k:/Andrew/vkr/example/f40k2/'
    list_c = os.listdir(path_f)
    mystat = []
    sum = 0
    for cat in list_c:
        len_cat =  len(os.listdir(path_f + cat))
        sum += len_cat
        mystat.append((int(cat), len_cat))
    print(mystat)
    print(len_cat)
    df = pd.DataFrame(data=mystat, columns=['0', '1'])
    df = df.sort(['1'], ascending=False)
    df.to_html('k:/Andrew/vkr/example/stat.html')

count_cat()
