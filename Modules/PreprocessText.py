import re
from nltk.corpus import stopwords


# input: string with text
# output: list with token words
def preprocess(text):
    text = text.replace('\n', '').lower()
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

# noun and Adjectives only
#def preprocess_NAD(text)
