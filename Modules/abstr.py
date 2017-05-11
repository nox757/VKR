import re
import os, sys
import string

import pandas as pd

import numpy as np
import pymorphy2
from numpy.lib.function_base import delete

morp=pymorphy2.MorphAnalyzer()

#path_f = 'k:/Andrew/vkr/example/f40k1a/'
path_f = 'k:/Andrew/vkr/example/f40k1a_with_name/'
path_rem = 'k:/Andrew/vkr/example/remove_f40k1.txt'
path_err = 'k:/Andrew/vkr/example/err_f40k2_csv_w_n.txt'
f_err = open(path_err, 'w', encoding='utf8')
path_csv = 'k:/Andrew/vkr/example/f40k1a_with_name.csv'
#path_cat = 'k:/Andrew/vkr/example/f40k1a_ravn500/'
path_cat = 'k:/Andrew/vkr/example/f40k1a_ravn100/'

def delete_files(path_rem, path_f):
    i = 0
    f_rem = open(path_rem, 'r', encoding='utf8')
    for line in f_rem:
        line = line.strip()
        if(line != ''):
            if os.path.isfile(path_f+line):
                os.remove(path_f+line)
                print(line)
                i += 1
    print(i)
    f_rem.close()


def make_csv(path_f):
    df = pd.DataFrame(columns=['0','1','2'])
    list_f = os.listdir(path_f)
    for el in list_f:
        f = open(path_f+el, 'r', encoding='utf8')
        str1 = str(re.match(r'\d\d', f.readline()).group(0))
        str2 = f.readline().strip()
        str3 = f.readline()
        if (str2 != '' and str3 != ''):
            df.loc[len(df)] = [str1, str2, str3]
        else:
            f_err.write(el, + '\n')
        f.close()
    print(len(df))
    df.to_csv('k:/Andrew/vkr/example/f40k1a_with_name.csv', encoding='utf8')

def eject_cat(path_csv, path_cat): #break into categories
    df = pd.read_csv(path_csv, encoding='utf8', usecols=['0', '1'])
    list_cat = df['0'].drop_duplicates().values
    df = df.groupby(['0'])
    for cat in list_cat:
        try:
            df1 = df.get_group(cat)
            flag = len(df1)
            if(flag > 100):
                df1 = df1[:100]
                df1.to_csv(path_cat + str(cat)+'.csv', encoding='utf8')
        except:
            f_err.write(str(cat)+'\n')
            pass

###reading big csv without problem with RAM return DataFrame
def read_csv(path_csv):
    mylist = []
    for chunk in pd.read_csv(path_csv, encoding='utf-8', chunksize=2000):
        mylist.append(chunk)
    df = pd.concat(mylist, axis=0)
    del mylist
    return  df

###summurize absract with text of article, combine in one dataframe
def concat_pd():
    df1 = read_csv(path_csv)[['1','2']]
    df2 = read_csv('k:/Andrew/vkr/example/f40k_csv_ravn100/6.csv')[['0','1','2']]
    print(len(df2))
    df1['1'] = df1['1'].str.lower().str.strip()
    df2['1'] = df2['1'].str.lower().str.strip()
    df3 = df2.merge(df1,'left', on='1')
    df3.rename(columns={'2_x':'2', '2_y':'3'}, inplace=True)
    print(len(df3))
    print(len(df3[df3['3'].isnull()]))
    # df3.to_csv('k:/Andrew/vkr/example/probe1.csv',encoding='utf8')
    # df2.to_csv('k:/Andrew/vkr/example/probe2.csv', encoding='utf8')
    print(df3['2'].duplicated())
    print(df3.loc[26:29])
    #df3.to_csv('k:/Andrew/vkr/example/40k2_concat.csv', encoding='utf8')
   # print(df1.loc[df1['1'].isin(df2['1'])]['2'])




#df = pd.read_csv('k:/Andrew/vkr/example/f40k1a.csv', encoding='utf8', usecols=['0','1'])
#print(df.head())
#eject_cat(path_csv, path_cat)

concat_pd()
# df = read_csv(path_csv)[['0', '1', '2']]
# df['1'] = df['1'].str.lower().str.strip()
# print(df.head())
# df = read_csv('k:/Andrew/vkr/example/40k2_concat.csv')
# print(df.loc[36547])

f_err.close()