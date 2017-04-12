import re
import os, sys
import string

import pandas as pd
import numpy as np


path_f = 'k:/Andrew/vkr/example/f40k1a/'
path_rem = 'k:/Andrew/vkr/example/remove_f40k1.txt'
path_err = 'k:/Andrew/vkr/example/err_f40k1a_csv_cat.txt'
f_err = open(path_err, 'w', encoding='utf8')
path_csv = 'k:/Andrew/vkr/example/f40k1a.csv'
path_cat = 'k:/Andrew/vkr/example/f40k1a_ravn500/'

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
    df = pd.DataFrame(columns=['0','1'])
    list_f = os.listdir(path_f)
    for el in list_f:
        f = open(path_f+el, 'r', encoding='utf8')
        str1 = str(re.match(r'\d\d', f.readline()).group(0))
        str2 = f.readline()
        if (str2 != ''):
            df.loc[len(df)] = [str1, str2]
        else:
            f_err.write(el, + '\n')
        f.close()
    print(len(df))
    df.to_csv('k:/Andrew/vkr/example/f40k1a.csv', encoding='utf8')

def eject_cat(path_csv, path_cat): #break into categories
    df = pd.read_csv(path_csv, encoding='utf8', usecols=['0', '1'])
    list_cat = df['0'].drop_duplicates().values
    df = df.groupby(['0'])
    for cat in list_cat:
        try:
            df1 = df.get_group(cat)
            flag = len(df1)
            if(flag > 500):
                df1 = df1[:500]
                df1.to_csv(path_cat + str(cat)+'.csv', encoding='utf8')
        except:
            f_err.write(str(cat)+'\n')
            pass



df = pd.read_csv('k:/Andrew/vkr/example/f40k1a.csv', encoding='utf8', usecols=['0','1'])
print(df.head())
eject_cat(path_csv, path_cat)


f_err.close()