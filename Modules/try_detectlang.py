import re
import os, sys
import string
from langdetect import detect

path_f = 'k:/Andrew/vkr/example/f1001/'
path_err = 'k:/Andrew/vkr/example/err2_f1001.txt'
path_out = 'k:/Andrew/vkr/example/f1002/'
i = 1


while i <= 1614:
   
        f = open(path_f + str(i) + '.txt', 'r', encoding='utf-8')
        str00 = f.readline() 
       
        str1 = f.readline()
        str2 = f.read().replace('\n', ' ')
        str2 = str2.lower()
        print(i, detect(str(str2)))
        f.close()
    
     
       
        i = i + 1


