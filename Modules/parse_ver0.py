import sys
import re
import os
import lxml
from bs4 import BeautifulSoup

i = 0
path_f = 'k:/Andrew/vkr/example/f1000/'
path_out = 'k:/Andrew/vkr/example/f1001/'
path_err = 'k:/Andrew/vkr/example/err_f1001.txt'
f_err = open(path_err, 'w', encoding='utf8')
list_f = os.listdir(path_f)
for el in list_f:
    path_full = path_f + el
    f = open(path_full, 'rb')
    soup = BeautifulSoup(f, "lxml")
    i = i + 1
    try:
        full_out = path_out + str(i) + '.txt'
        f_out = open(full_out, 'w', encoding='utf8')
        
        for strong_tag in soup.find('ul', 'codes-list').find_all('span'):
            if strong_tag.text == 'ГРНТИ: ':
                s = strong_tag.next_sibling
##                ss = re.match(r'\d\d', s)
##                print(s, ss.group(0))
                f_out.write(s + '\n')
        souph = soup.find('span', itemprop='headline').get_text().replace('\n', ' ')
        f_out.write(souph) 
        soup1 = soup.find('p', itemprop='articleBody').get_text()
        #soup1 = soup1.replace('\n', ' ')
        f_out.write(soup1 + '\n')
        f_out.close()
    except:
        f_err.write(str(i) + '\n')
        pass
    f.close()
f_err.close()









##for fi in range(len(list_f)):
##    if fi == 0:
##        path_full = path_f + list_f[fi]
##        f = open(path_full, 'rb')
##        soup = BeautifulSoup(f, "lxml")
##        print(soup)



##f = open('k:/Andrew/vkr/example/1.htm', 'rb')
##soup = BeautifulSoup(f, "lxml")
##
##
##
##for strong_tag in soup.find('ul', 'codes-list').find_all('span'):
##    if strong_tag.text == 'ГРНТИ: ':
##        print (strong_tag.next_sibling.replace(' ',''))
##soup1 = soup.find('p', itemprop='articleBody').get_text()
##print (soup1)
