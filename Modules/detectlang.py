import re
import os, sys
import string
from langdetect import detect
import chardet

#lang which was using for cyberleninka
def lang1():
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




####trying other encoding with resoureces
encodings = {
    'UTF-8':      'utf-8',
    'CP1251':     'windows-1251',
    'KOI8-R':     'koi8-r',
    'IBM866':     'ibm866',
    'ISO-8859-5': 'iso-8859-5',
    'MAC':        'mac',
}

#"""
#Определение кодировки текста
#"""
def get_codepage(str = None):
    uppercase = 1
    lowercase = 3
    utfupper = 5
    utflower = 7
    codepages = {}
    for enc in encodings.keys():
        codepages[enc] = 0
    if str is not None and len(str) > 0:
        last_simb = 0
        for simb in str:
            simb_ord = ord(simb)

            #"""non-russian characters"""
            if simb_ord < 128 or simb_ord > 256:
                continue

            #"""UTF-8"""
            if last_simb == 208 and (143 < simb_ord < 176 or simb_ord == 129):
                codepages['UTF-8'] += (utfupper * 2)
            if (last_simb == 208 and (simb_ord == 145 or 175 < simb_ord < 192)) \
                or (last_simb == 209 and (127 < simb_ord < 144)):
                codepages['UTF-8'] += (utflower * 2)

            #"""CP1251"""
            if 223 < simb_ord < 256 or simb_ord == 184:
                codepages['CP1251'] += lowercase
            if 191 < simb_ord < 224 or simb_ord == 168:
                codepages['CP1251'] += uppercase

            """KOI8-R"""
            if 191 < simb_ord < 224 or simb_ord == 163:
                codepages['KOI8-R'] += lowercase
            if 222 < simb_ord < 256 or simb_ord == 179:
                codepages['KOI8-R'] += uppercase

            """IBM866"""
            if 159 < simb_ord < 176 or 223 < simb_ord < 241:
                codepages['IBM866'] += lowercase
            if 127 < simb_ord < 160 or simb_ord == 241:
                codepages['IBM866'] += uppercase

            """ISO-8859-5"""
            if 207 < simb_ord < 240 or simb_ord == 161:
                codepages['ISO-8859-5'] += lowercase
            if 175 < simb_ord < 208 or simb_ord == 241:
                codepages['ISO-8859-5'] += uppercase

            """MAC"""
            if 221 < simb_ord < 255:
                codepages['MAC'] += lowercase
            if 127 < simb_ord < 160:
                codepages['MAC'] += uppercase

            last_simb = simb_ord

        idx = ''
        max = 0
        for item in codepages:
            if codepages[item] > max:
                max = codepages[item]
                idx = item
        return idx

#lang which using for e-library
def lang2():
    path_f = 'k:\Andrew\\vkr\elib\90\\'
    for el in os.listdir(path_f):
        f = open(path_f+el, 'r', errors='ignore')
        ##readall file
        fl = 0
        str0 = f.read()
        lng = detect(str0)
        sum = 0
        if (lng == 'ru'):
            sum += 1
            print(str0)
        print (lng)
        print (sum)
        f.close()

def converter(filePath):
    #if any([filePath.endswith(extension) for extension in '.srt,.ass,.txt'.split(',')]):
        with open(filePath, "rb") as F:
            for text in F:

                enc = chardet.detect(text).get("encoding")
                print (text)
               # if enc and enc.lower() != "utf-8":
                try:
                    text = text.decode(enc)
                    text = text.encode("utf-8")
                    print (text.decode('cp1252'))
                    # with open(filePath+"1.txt", "ab") as f:
                    #     f.write(text)
                    #     print (u"%s сконвертирован." % filePath)
                except:
                    print (u"Ошибка в имени файла: название содержит русские символы.")
                # else :
                #     print (u"Файл %s находится в кодировке %s и не требует конвертирования." % (filePath, enc))
                #     print(text)
                print ('-'*40)

def try_decode(path_f):
    import re, itertools

    path_f = 'k:\Andrew\\vkr\elib\90\\'
    for el in os.listdir(path_f)[:1]:
        f = open(path_f+el, 'rb')
        s = "Çàâîäcêàÿ ëàáîpàòîpèÿ. Äèàãíîcòèêà ìàòåpèàëîâ». Ñïåöèàëüíûé âûïóñê"
        encodings = ['cp1251', 'cp1252', 'utf8']

        for enc1 in encodings:
            for enc2 in encodings:
                r = s
                try:
                    r = r.encode(enc1).decode(enc2)

                    if re.match('[а-яА-ЯёЁ]+[а-яА-ЯёЁ]+', r):
                        print( enc1, enc2, r)
                except (UnicodeEncodeError, UnicodeDecodeError) as e:
                    pass

        f.close()


#lang2()
path_f = 'k:\Andrew\\vkr\elib\90\\elibrary_11601220_63143288.txt'
# #path_f = 'k:\Andrew\\vkr\elib\90\\elibrary_11806988_77474954.txt'
#converter(path_f)
try_decode(path_f)
