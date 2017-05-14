import re
import os

from nltk.corpus import stopwords

import pymorphy2

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

import docx  ##package pip3 install python-docx
# input: string with text
# output: list with token words or None
def preprocess(text):
    text = text.replace('\n', ' ').lower()
    str = re.findall(r"\b([а-яё]+)", text)
    res = []
    for el in str:
        el = el.strip()
        if len(el) > 3:
            res.append(el)
    if res != []:
        return res
    else:
        return None

#return str with only nouns and adj
#input: string with token words
def get_only_NAD(text):
    morp = pymorphy2.MorphAnalyzer()
    list_text = text.split(' ')
    newstr = ""
    if list_text == []:
        return None
    else:
        for word in list_text:
            if len(word) > 3:
                morp_list = morp.parse(word)[0].tag
                if ('NOUN' in morp_list) or ('ADJF' in morp_list):
                    newstr.append(morp.normal_forms(word)[0])
        return newstr

#read from pdf file to string, but problem with some codes differ from 'utf8'
#                                   and files wtih specific fonts((
def read_from_pdf(path_f):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    f = open(path_f, 'rb')
    process_pdf(rsrcmgr, device, f)
    f.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str.replace('-\n', '').replace('\n',' ')

def read_from_docx(path_f):
    doc = docx.Document(path_f)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def read_from_txt(path_f):
    f = open(path_f, 'r' , errors='ignore')
    text = f.read()
    f.close()
    return  text

pathf = 'k://Andrew//vkr//elib//1.docx'

print(read_from_docx(pathf))
#enc = chardet.detect(text).get("encoding")
# print (text)
