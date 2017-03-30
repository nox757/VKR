import nltk
from nltk.corpus import stopwords
import pandas as pd
import csv
import codecs
import numpy as np
import string
import sys
import matplotlib




csv.field_size_limit(sys.maxsize)
stop_words = stopwords.words('russian')
#k:/Andrew/vkr/example/1600.csv
output_file = open("k:/Andrew/vkr/example/1600.csv", 'r')
csv_out = csv.reader(output_file)
raw_data = []
for row in csv_out:
    if(row != []):
        raw_data.append(row)
output_file.close()
#df = pd.read_csv(raw_data, header=None, error_bad_lines=False)
#print(raw_data)
#f.close()
df = pd.DataFrame(raw_data)
df.to_csv('probe1.csv', encoding='utf-8')
df1 = pd.read_csv('probe1.csv',encoding='utf-8')
df1 = df1.dropna()
print(df1['2'].apply(lambda x: len(x.split(' '))).sum())

