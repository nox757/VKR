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
#k:/Andrew/vkr/example/40k1.csv
# output_file = open("k:/Andrew/vkr/example/40k1.csv", 'r')
# csv_out = csv.reader(output_file)
# raw_data = []
# for row in csv_out:
#     if(row != []):
#         raw_data.append(row)
# output_file.close()
#
# df1 = pd.DataFrame(raw_data)
# df1 = df1.dropna()

# df1.to_csv('k:/Andrew/vkr/example/40k1_pandas.csv',encoding='utf-8')

#print(df1['2'].apply(lambda x: len(x.split(' '))).sum()) ## count words in all test
# my_tags= []
# for el in df1['0'].drop_duplicates():
#     my_tags.append(str(el))
#
# df1['0'].value_counts().plot(kind="bar",rot = 0)
#
# plt.show()

