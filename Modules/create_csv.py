import csv
import os
import re
from nltk.corpus import stopwords
import nltk
import string

output_file = open("k:/Andrew/vkr/example/40k2_notCl.csv", 'w')
csv_out = csv.writer(output_file)
path_f = 'k:/Andrew/vkr/example/f40k2_notCl/'
path_err = 'k:/Andrew/vkr/example/err2_40k2_notCl_csv.txt'
f_err = open(path_err, 'w', encoding='utf-8')
list_f = os.listdir(path_f)
stop_words = stopwords.words('russian')

for el in list_f:
    try:
        f = open(path_f + el, 'r', encoding='utf-8')
        struct = []
        str0 = f.readline()
        struct.append(str0.strip())
        str1 = f.readline()
        struct.append(str1.strip())

        str2 = f.read().replace('\n', ' ')
        res = str2.split(' ')
        res = [i for i in res  if len(i) > 3 and ( i not in stop_words )]
        str2 = ' '.join(res)
        struct.append(str2.strip())
        csv_out.writerow(struct)
        f.close()
    except:
        f_err.write(str(el) + '\n')
        f.close()
        pass
f_err.close()
output_file.close()



# output_file = open("k:/Andrew/vkr/example/40k.csv", 'r')
# csv_out = csv.reader(output_file, delimiter=',')
# for row in csv_out:
#     if(row != []):
#         print(row[0])
# output_file.close()