import nltk
from nltk.corpus import stopwords
import pandas as pd
import csv
import codecs
import numpy as np
import string
import sys
import matplotlib.pyplot as plt
import os


path_f = 'k:/Andrew/vkr/example/f40k2_concat_ravn500/'
path_err = 'k:/Andrew/vkr/example/err2_40k2__ravn500_concat.txt'
f_err = open(path_err, 'w', encoding='utf-8')
mylist = []
# for chunk in  pd.read_csv('k:/Andrew/vkr/example/40k2_notCl_pandas.csv', encoding='utf-8', chunksize=2000):
for chunk in  pd.read_csv('k:/Andrew/vkr/example/40k2_concat.csv', encoding='utf-8', chunksize=2000):
    mylist.append(chunk)
df = pd.concat(mylist, axis= 0)
del mylist
categ = df['0'].drop_duplicates().values
del df[df.columns[0]]
print (len(df))
print(len(df[df['3'].isnull()]))
df.dropna(axis=0, how='any', inplace=True)
print (len(df))
print(df.columns[0])
df = df.groupby(['0'])
for cat in categ:
    try:
        df1 = df.get_group((cat))
        fl_count = len(df1)
        print(fl_count)
        if(fl_count >= 500):
            df1 = df1[:500]
            df1.to_csv(path_f+str(cat)+'.csv', encoding='utf-8')
    except:
        f_err.write(str(cat)+'\n')
        pass
f_err.close()
