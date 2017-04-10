import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
import pandas as pd
import csv
import codecs
import numpy as np
import string
import sys
import matplotlib.pyplot as plt
import os
import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn import  linear_model
import sklearn

import scipy
from sklearn import metrics
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
import datetime as dt
import itertools

def pltConfus_matrix (matrix, tagret, title="Confusion matrix", cmp= plt.cm.Blues, path_f=os.getcwd()):
    plt.imshow(matrix,interpolation='nearest', cmap=cmp)
    plt.title(title)
    plt.colorbar()
    plt.savefig(path_f)
    tick_marks = np.arange(len(tagret))
    plt.xticks(tick_marks, tagret, rotation=45)
    plt.yticks(tick_marks, tagret)

    thresh = matrix.max() / 2.
    for i, j in itertools.product(range(matrix.shape[0]), range(matrix.shape[1])):
        plt.text(j, i, matrix[i, j],
                 horizontalalignment="center",
                 color="white" if matrix[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig(path_f+"\\graphics.png")

#return name of txt file with metrics
def metricsToFile(tagret, predict, path = os.getcwd()):
    dates = dt.datetime.strftime(dt.datetime.now(), "%Y%m%d_%H%M")
    file = open(path +"\\"+ str(dates) + ".txt", 'a', encoding='utf-8')
    file.write(dates + '\n')
    file.write(metrics.classification_report(tagret, predict))
    file.write(repr(metrics.confusion_matrix(tagret, predict)))
    file.write('\n')
    file.close()
    return dates

#return path of folder with model
def modelToFile(model, name="Noname", path=os.getcwd()):
    path_f = path + name
    if not os.path.exists(path_f):
        os.mkdir(path_f)
    joblib.dump(model, str(path_f)+"\\"+name+".mdl")
    return path_f

def modelFromFile(name="Noname", path=os.getcwd()):
    load_model = joblib.load(str(path)+"\\"+name + ".mdl")
    return load_model

def strtofile(name="Noname file", path_f=os.getcwd(), str=""):
    with open(path_f + "\\"+name+".txt", "a", encoding='utf-8') as text_file:
        print(str, file=text_file)

csv.field_size_limit(sys.maxsize)
plt.interactive(False)
#path_f = 'k:/Andrew/vkr/example/f40k_csv_ravn_NA/'
path_f = 'k:/Andrew/vkr/example/f40k_csv_ravn100/'
path_model = 'K:\\Andrew\\Programming\\VKR\\Results\\'

list_f = os.listdir(path_f)
data = pd.DataFrame()
for el in list_f:
    df = pd.read_csv(path_f+el, encoding='utf-8', usecols=['0','1','2'])
    data = data.append(df, ignore_index=True)
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
print(len(train_data))

clf_text = Pipeline([
    ('cntvec' ,CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('logreg', linear_model.LogisticRegression(n_jobs=1, C=1e5)),
    ])

clf_text = clf_text.fit(train_data['2'], train_data['0'])

print(len(clf_text.named_steps['cntvec'].get_feature_names()))

path_mdl = modelToFile(clf_text, "Probe_100", path_model)
#clf_text = modelFromFile("Probe", path_mdl)

predicted =  clf_text.predict(test_data['2'])
file_metr = metricsToFile(test_data['0'], predicted, path_mdl)
print(np.mean(predicted == test_data['0']))


cnf_matrix = metrics.confusion_matrix(test_data['0'], predicted)
plt.figure()
pltConfus_matrix(matrix=cnf_matrix, tagret=clf_text.classes_,
                      title='Confusion matrix LR', path_f=path_mdl)
plt.show()
strtofile(name=file_metr,path_f=path_mdl,str="count words:"+str(len(clf_text.named_steps['cntvec'].get_feature_names())))