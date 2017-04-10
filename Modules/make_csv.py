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


path_f = 'k:/Andrew/vkr/example/f40k_csv_ravn100/'
path_err = 'k:/Andrew/vkr/example/err2_40k2__ravn100_notCl_pandasToCsv.txt'
f_err = open(path_err, 'w', encoding='utf-8')
mylist = []
for chunk in  pd.read_csv('k:/Andrew/vkr/example/40k2_notCl_pandas.csv', encoding='utf-8', chunksize=2000):
    mylist.append(chunk)
df = pd.concat(mylist, axis= 0)
del mylist
categ = df['0'].drop_duplicates().values
# print(categ)
del df[df.columns[0]]
print(df.columns[0])
df = df.groupby(['0'])
for cat in categ:
    try:
        df1 = df.get_group((cat))
        fl_count = len(df1)
        print(fl_count)
        if(fl_count >= 100):
            df1 = df1[:100]
            df1.to_csv(path_f+str(cat)+'.csv', encoding='utf-8')
    except:
        f_err.write(str(cat)+'\n')
        pass
f_err.close()
