import re
import os, sys
import string
from langdetect import detect

path_f = 'k:/Andrew/vkr/example/f40k1/'
path_rem = 'k:/Andrew/vkr/example/remove_f40k1.txt'
path_out = 'k:/Andrew/vkr/example/f1002/'
i = 1
list_f = os.listdir(path_f)
f_rem = open(path_rem, 'w', encoding='utf-8')
s = ""
for el in list_f:
   
        f = open(path_f + el,'r', encoding='utf-8')
        ##readall file
        fl = 0
        try:
                str0 = f.read()
                if detect(str0) != 'ru':
                    f.close()
                    fl = 1
                    os.remove(path_f+el)
                    f_rem.write(el + '\n')
        except:
                f_rem.write(str(el) +' err\n' )
                pass
        if(fl == 0):
            f.close()
f_rem.close()


