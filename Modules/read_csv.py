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


path_f = 'k:/Andrew/vkr/example/f40k_csv_ravn/'
path_err = 'k:/Andrew/vkr/example/err2_40k2_notCl_pandasToCsv.txt'
f_err = open(path_err, 'w', encoding='utf-8')
# mylist = []
# for chunk in  pd.read_csv('k:/Andrew/vkr/example/40k2_notCl_pandas.csv', encoding='utf-8', chunksize=2000):
#     mylist.append(chunk)
# df = pd.concat(mylist, axis= 0)
# del mylist
# categ = df['0'].drop_duplicates().values
# # print(categ)
# del df[df.columns[0]]
# print(df.columns[0])
# df = df.groupby(['0'])
list_f = os.listdir(path_f)
result = pd.DataFrame()

for el in list_f:###read all data to 'result' 0-GRNTI, 1-Name Article, 2-Text
    try:
        df = pd.read_csv(path_f+el, encoding='utf-8',usecols=["0", "1", "2"])

        result = result.append(df, ignore_index=True)

    except:
        f_err.write(str(el)+'\n')
        pass
#to get only array of values:
#       result["Name column in qoutes"].values
print(result[["0","1"]])
f_err.close()
