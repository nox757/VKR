import re
import os, sys
import string

path_f = 'k:/Andrew/vkr/example/f1001/'
path_err = 'k:/Andrew/vkr/example/err2_f1001.txt'
path_out = 'k:/Andrew/vkr/example/f1002/'
i = 1

f_err = open(path_err, 'w', encoding='utf-8')
while i <= 1614:
    try:
        f = open(path_f + str(i) + '.txt', 'r', encoding='utf-8')
        str00 = f.readline()
        str0 = str(re.match(r'\d\d', str00).group(0))
        if not os.path.exists(path_out + str0):
            os.mkdir(path_out + str0)
        f_out = open(path_out + str0 + '\\' + str(i) + '.txt', 'w', encoding='utf-8')
        str1 = f.readline()
        f_out.write(str00) # str all name category and code
        f_out.write(str1) # str name article
        str2 = f.read().replace('\n', ' ')
        str2 = str2.lower()
        res = re.findall(r"\b([а-яё]+)", str2)
        str2 = ' '.join(res)
        f_out.write(str2 + '\n')
        f_out.close()
        f.close()
    except:
        f_err.write(str(i) + '\n')
        pass
    i = i + 1

f_err.close()
