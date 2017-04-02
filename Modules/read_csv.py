
import pandas as pd
import csv
import codecs
import numpy as np
import string
import sys

import os
import pymorphy2 as py

path_f = 'k:/Andrew/vkr/example/f40k_csv_ravn/'
path_f2 = 'k:/Andrew/vkr/example/f40k_csv_ravn_NA/'
path_err = 'k:/Andrew/vkr/example/err2_40k2_notCl_pandasToCsv.txt'
f_err = open(path_err, 'w', encoding='utf-8')

list_f = os.listdir(path_f)



morp = py.MorphAnalyzer()
for el in list_f[0:5]:###read all data to 'result' 0-GRNTI, 1-Name Article, 2-Text
    try:
        result = pd.DataFrame()
        df = pd.read_csv(path_f+el, encoding='utf-8',usecols=["0", "1", "2"])
        result = result.append(df, ignore_index=True)
        for i in result.index:
            try:
                text = result.iat[i, 2].split(' ')
                mod_text = []
                for word in text:
                    morp_list = morp.parse(word)[0].tag
                    if ('NOUN' in morp_list) or ('ADJF' in morp_list):
                        mod_text.append(morp.normal_forms(word)[0])
                result.iat[i, 2] = " ".join(mod_text)
                print(el +"_"+str(i))
            except:
                f_err.write("i"+str(el)+"_"+str(i)+'\n')
                pass
        result.to_csv(path_f2 + el, encoding='utf-8')
        print(el+"_end")
    except:
        f_err.write(str(el)+'\n')
        pass
f_err.close()

