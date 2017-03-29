import re
import lxml
#from html5lib import treebuilders
#f = open('k:/Andrew/vkr/example/1.htm', 'rb')
#lxml_etree_document = html5lib.parse(f, treebuilder="lxml")
#print (lxml_etree_document)
from bs4 import BeautifulSoup
f = open('k:/Andrew/vkr/example/1.htm', 'rb')
soup = BeautifulSoup(f, "lxml")
#print (soup.find('div', 'col-right'))
 
#print (soup.find('p', itemprop='articleBody'))
#print (soup.find('ul', 'codes-list'))


for strong_tag in soup.find('ul', 'codes-list').find_all('span'):
    if strong_tag.text == 'ГРНТИ: ':
        s = strong_tag.next_sibling.replace(' ','')
        print(s)
        ss = re.match(r'\d\d', s)
        print (ss.group())
        
soup1 = soup.find('span', itemprop='headline').get_text().replace('\n', ' ')
print (soup1)
