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






plt.interactive(False)
path_f = 'k:/Andrew/vkr/example/f40k2/'
list_c = os.listdir(path_f)
mystat = []
for cat in list_c:
    mystat.append((int(cat),len(os.listdir(path_f+cat))))
print(mystat)
df = pd.DataFrame(data=mystat, columns=['0', '1'])
df = df.sort(['1'], ascending=False)

print(df.head())
plt.figure(figsize=(20,5))
df['1'].plot(kind='bar',rot=0).set_xticklabels(df['0'])
plt.show()

