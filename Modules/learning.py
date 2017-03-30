import nltk
from nltk.corpus import stopwords
import pandas as pd
import csv
import codecs
import numpy as np
import string
import sys
import matplotlib.pyplot as plt


plt.interactive(False)
csv.field_size_limit(sys.maxsize)
stop_words = stopwords.words('russian')
#k:/Andrew/vkr/example/1600.csv

df1 = pd.read_csv('probe1.csv',encoding='utf-8')
df1 = df1.dropna()
#print(df1['2'].apply(lambda x: len(x.split(' '))).sum()) ## count words in all test
my_tags= []
for el in df1['0'].drop_duplicates():
    my_tags.append(str(el))

df1['0'].value_counts().plot(kind="bar",rot = 0)

plt.show()

