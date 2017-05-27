import re

from nltk.corpus import stopwords

import pymorphy2

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

import docx  ##package pip3 install python-docx
import chardet

# input: string with text
# output: list with token words or None
def preprocess(text):

    text = text.replace('\n', ' ').lower()
    str = re.findall(r"\b([а-яё]+)", text)
    stop_words = stopwords.words('russian')
    res = str
    res = [i for i in res  if len(i) > 3 and ( i not in stop_words )]
    if res != []:
        return res
    else:
        return None


def get_only_normal(list_text):
    """return list with normal word
        input: string with token words"""
    morp = pymorphy2.MorphAnalyzer()
    new_list = []
    if list_text == []:
        return None
    else:
        for word in list_text:
            word = word.lower()
            if len(word) > 3:
                new_list.append(morp.normal_forms(word)[0])
        return new_list

def get_only_NAD(list_text):
    """return list with normal only nouns and adj
        input: list  with token words"""
    morp = pymorphy2.MorphAnalyzer()
    new_list = []
    if list_text == []:
        return None
    else:
        for word in list_text:
            word = word.lower()
            if len(word) > 3:
                morp_list = morp.parse(word)[0].tag
                if ('NOUN' in morp_list) or ('ADJF' in morp_list):
                    new_list.append(morp.normal_forms(word)[0])
        return new_list


def read_from_pdf(path_f):
    """ read from pdf file to string, but problem with some codes differ from 'utf8'
                                      and files wtih specific fonts(("""
    rsrcmgr = PDFResourceManager()
    strIO = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, strIO, laparams=laparams)
    f = open(path_f, 'rb')
    process_pdf(rsrcmgr, device, f)
    f.close()
    device.close()
    #get text with replace word wrap
    str = strIO.getvalue().replace('-\n', '')
    strIO.close()
    return str


def read_from_docx(path_f):
    doc = docx.Document(path_f)
    list_text = []
    text = ''
    for para in doc.paragraphs:
        list_text.append(para.text)
    if (list_text != []):
        text = '\n'.join(list_text)
    return text



def read_from_txt(path_f):
    f = open(path_f, 'rb')
    text = f.read()
    enc = chardet.detect(text).get("encoding")
    f.close()
    if enc:
        return  text.decode(enc, errors='ignore')
    else:
        return text.decode('utf8', errors='ignore')



def try_decode(text):
    """some files aftre extract may wrong codec,
    this func try fix it"""
    encodings = ['cp1251', 'cp1252', 'utf8']

    for enc1 in encodings:
        for enc2 in encodings:
            r = text
            try:
                r = r.encode(enc1).decode(enc2, errors='ignore')
                if re.search(r'\b[а-яА-Я]{3,}', r):
                    # some symbol in English code
                    r.replace('c', 'с').replace('p', 'р')
                    return r
            except (UnicodeEncodeError, UnicodeDecodeError) as e:
                pass
    return None



