import re
import os
import lxml
from bs4 import BeautifulSoup


path_f = 'k:/Andrew/vkr/example/f40k/'
path_out = 'k:/Andrew/vkr/example/f40k1a_with_name/'
path_err = 'k:/Andrew/vkr/example/err_f40k1a_with_name.txt'

f_err = open(path_err, 'w', encoding='utf8')

list_f = os.listdir(path_f)

i = 0
for el in list_f:
    i = i+1
    try:
        f = open(path_f+el, 'rb')
        soup = BeautifulSoup(f, "lxml")
        ## find GRNTI code
        s = ""
        for strong_tag in soup.find('ul', 'codes-list').find_all('span'):
            if strong_tag.text == 'ГРНТИ: ':
                s = strong_tag.next_sibling

        if (s != ""):
            souph = soup.find('span', itemprop='headline').get_text().replace('\n', ' ')
            soupA= soup.find('p', itemprop='description').get_text().replace('\n', ' ').strip().lower()
            res = re.findall(r"\b([а-яё]+)", soupA)
            if (len(res) > 4 and souph != ''):
                full_out = path_out + str(i) + '.txt'
                f_out = open(full_out, 'w', encoding='utf8')
                f_out.write(s + '\n')
                f_out.write(souph + '\n')
                f_out.write(' '.join(res)+'\n')
                f_out.close()
            else:
                f_err.write("f" + el + " " + str(i) + '\n') #few words
                print("f" + el + " " + str(i) + '\n')
        else:
            f_err.write("e" + el + " " + str(i) + '\n')  # empty GRNTI
            print("e" + el + " " + str(i) + '\n')
        f.close()

    except:
        f_err.write(el+" "+str(i)+'\n') #others errors
        print(el+" "+str(i)+'\n')
        pass
f_err.close()
