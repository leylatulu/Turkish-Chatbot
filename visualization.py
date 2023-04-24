import random
import json
import pickle
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# stop worda yükle

import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.stem import WordNetLemmatizer

# pip install tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

from unicode_tr import unicode_tr
from snowballstemmer import TurkishStemmer
from nltk import ngrams
from nltk.corpus import stopwords
import nltk
# nltk.download('punkt')

# warningleri kapatalım
import warnings

warnings.filterwarnings('ignore')

# veri setini yükleme
intents = json.loads(open("intense2 (1).json", encoding="utf-8", errors='ignore').read())

# veri setini temizleme
lemmatizer = WordNetLemmatizer

stemmer = TurkishStemmer()

words = []
classes = []
documents_X = []
documents_y = []
ignore_letters = ["?", "!", ".", ";", ",", ":", ":D", "-"]


def metin_onisle(metin):
    kucuk_harfli_metin = unicode_tr(metin).lower()
    istenen_karakterler = set(list(' abcdefghijklmnopqrstuvwxyzâçîöüğış0123456789'))
    harfler = list(kucuk_harfli_metin)
    harfler = [k if k in istenen_karakterler else ' ' for k in harfler]
    temiz_dokuman = "".join(kucuk_harfli_metin)
    temiz_dokuman_kelimeleri = temiz_dokuman.split(' ')
    temiz_dokuman_kelimeleri = [kelime for kelime in temiz_dokuman_kelimeleri if len(kelime) > 0]
    turkStem = TurkishStemmer()  # stemmer ile kelime köklerini buluyoruz
    temiz_dokuman_kelimeleri = [turkStem.stemWord(kelime) for kelime in temiz_dokuman_kelimeleri]
    n = 0  # n sayısı kadar kelimeyi birleştiriyoruz
    bigrams = ngrams(temiz_dokuman_kelimeleri, n)  # burada bigramlar ile kelimeleri birleştiriyoruz
    bigramstr = map(''.join, bigrams)
    ngram = " ".join(list(bigramstr))
    temiz_dokuman = " ".join(temiz_dokuman_kelimeleri) + " " + "".join(ngram)
    return temiz_dokuman


# tüm patternslar için wordcloud
# tüm patternsları çek
all_patterns = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        # tokenize each word
        w = nltk.word_tokenize((pattern))
        words.extend(w)
        # add documents in the corpus
        documents_X.append((w, intent["tag"]))
        # add to our classes list
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# stop wordsleri sil
sw = stopwords.words('turkish')
words = [w for w in words if not w in sw]

len(words)
"""
#Normal wordcloud
text = " ".join(words)
wordcloud = WordCloud(max_font_size=50, max_words=50, background_color="white").generate(text)
plt.figure(figsize=(15, 15))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show(block=True)
"""
from PIL import Image

vbo_mask = np.array(Image.open("miuul.png"))
# kelimelerin net görünmesi için
wc = WordCloud(background_color="white", max_words=500, mask=vbo_mask, contour_width=2, contour_color='steelblue')

# generate word cloud
def generate_word_cloud():
    text = " ".join(words)
    wordcloud = WordCloud(max_font_size=500, max_words=500,
                          background_color="white", mask=vbo_mask,
                          contour_width=2).generate(text)
    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show(block=True)
# generate word cloud
generate_word_cloud()



# N-gramları görselleştirme
def get_top_n_tri_gram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(3, 3)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]

from sklearn.feature_extraction.text import CountVectorizer

common_words = get_top_n_tri_gram(words, 20)
import pandas as pd
df1 = pd.DataFrame(common_words, columns=['words', 'count'])

df1.groupby('words').sum()['count'].sort_values(ascending=False).plot(
    kind='bar', title='En Çok Kullanılan 3-gramlar')









