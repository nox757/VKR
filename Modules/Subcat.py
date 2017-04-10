# import nltk
# from nltk.corpus import stopwords
# from sklearn.model_selection import train_test_split
# import pandas as pd
# import csv
# import codecs
# import numpy as np
# import string
# import sys
# import matplotlib.pyplot as plt
import os
# import tqdm
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.linear_model import LogisticRegression
# from sklearn import  linear_model
# import sklearn
# import scipy
# from sklearn import metrics
# from sklearn.externals import joblib
# from sklearn.pipeline import Pipeline
# import datetime as dt
# import itertools
import re

path_f = 'k:/Andrew/vkr/example/f40k2/'
path_err = 'k:/Andrew/vkr/example/err_subcat06.txt'
path_out = 'k:/Andrew/vkr/example/sub06/'

f_err = open(path_err, 'w', encoding='utf-8')
list_c = os.listdir(path_f)

i = 0
for cat in list_c:
    i = 0
    list_f = os.listdir(path_f+cat)
    for el in list_f:
        try:
            f = open(path_f +cat+"\\"+ el, 'r', encoding='utf-8')
            str00 = f.readline()
            if(re.findall(r'\d\d', str00)[1] != ''):
                i += 1
            f.close()
        except:
            f_err.write(str(el) + '\n')
            pass
    print(i, cat)
f_err.close()