import re
import os
import lxml
from bs4 import BeautifulSoup


path_f = 'k:/Andrew/vkr/example/f40k/'
path_out = 'k:/Andrew/vkr/example/f40k1a/'
path_err = 'k:/Andrew/vkr/example/err_f40k1a.txt'

f_err = open(path_err, 'w', encoding='utf8')

list_f = os.listdir(path_f)

i = 0
for el in list_f:
    i = i+1
    try:
        f = open(path_f+el, 'rb')
        soup = BeautifulSoup(f, "lxml")
        full_out = path_out + str(i) + '.txt'
        f_out = open(full_out, 'w', encoding='utf8')
        ## find GRNTI code
        s = ""
        for strong_tag in soup.find('ul', 'codes-list').find_all('span'):
            if strong_tag.text == 'ГРНТИ: ':
                s = strong_tag.next_sibling
                f_out.write(s + '\n')
        if (s != ""):
            soupA= soup.find('p', itemprop='description').get_text().replace('\n', ' ').strip().lower()
            res = re.findall(r"\b([а-яё]+)", soupA)
            if (len(res) > 4):
                f_out.write(' '.join(res)+'\n')
            else:
                f_err.write("f" + el + " " + str(i) + '\n') #few words
        else:
            f_err.write("e" + el + " " + str(i) + '\n')  # empty GRNTI
        f_out.close()
        f.close()

    except:
        f_err.write(el+" "+str(i)+'\n')
        pass
f_err.close()
