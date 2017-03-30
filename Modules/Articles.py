import pymorphy2
import os


morp=pymorphy2.MorphAnalyzer()

path_f = 'k:/Andrew/vkr/example/f40k2_notCl/'
path_err = 'k:/Andrew/vkr/example/err2_f40k2n_adj.txt'
path_out = 'k:/Andrew/vkr/example/f40k2n_adj/'

f_err = open(path_err, 'w', encoding='utf-8')
list_f = os.listdir(path_f)
for el in list_f:
    try:
        f = open(path_f + el, 'r', encoding='utf-8')
        str0 = f.readline()
        if not os.path.exists(path_out):
            os.mkdir(path_out)
        f_out = open(path_out + el, 'w', encoding='utf-8')
        str1 = f.readline()
        f_out.write(str0)  # str all name category and code
        f_out.write(str1)  # str name article
        str2 = f.read().replace('\n', ' ')

        newstr = []
        for word in str2.split(' '):
            if ('NOUN' in morp.parse(word)[0].tag) or ('ADJF' in morp.parse(word)[0].tag):
                newstr.append(morp.normal_forms(word)[0])
        str2 = ' '.join(newstr)
        f_out.write(str2 + '\n')
        f_out.close()
        f.close()
    except:
        f_err.write(el+'\n')
        pass
f_err.close()