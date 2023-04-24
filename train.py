import random
import json
import pickle
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
# pip install tensorflow
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD, Adam
from keras.models import load_model
from unicode_tr import unicode_tr
#from snowballstemmer import TurkishStemmer
from nltk.stem import WordNetLemmatizer
from nltk import ngrams
from nltk.corpus import stopwords
import nltk
# nltk.download('punkt')

import warnings
warnings.filterwarnings('ignore')

intents = json.loads(open("intents.json", encoding="utf-8", errors='ignore').read())


lemmatizer = WordNetLemmatizer()
#stemmer = TurkishStemmer()

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
    temiz_dokuman_kelimeleri = [lemmatizer.lemmatize(kelime) for kelime in temiz_dokuman_kelimeleri]
    n = 2 
    bigrams = ngrams(temiz_dokuman_kelimeleri, n)
    bigramstr = map(''.join, bigrams)
    ngram = " ".join(list(bigramstr))
    temiz_dokuman = " ".join(temiz_dokuman_kelimeleri) + " " + "".join(ngram)
    return temiz_dokuman


# tüm patternslar
all_patterns = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        # tokenize each word
        w = nltk.word_tokenize((pattern))
        words.extend(w)
        # burada
        documents_X.append((w, intent["tag"]))
        # add to our classes list
        if intent["tag"] not in classes:
            classes.append(intent["tag"])


sw = stopwords.words('turkish')
words = [w for w in words if not w in sw]

len(words)

text = " ".join(words)
wordcloud = WordCloud(max_font_size=150, max_words=500, background_color="white").generate(text)
plt.figure(figsize=(15, 15))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show(block=True)

from PIL import Image

vbo_mask = np.array(Image.open("VBO - Kopya.jpg"))
wc = WordCloud(background_color="white", max_words=800, mask=vbo_mask)


# generate word cloud
def generate_word_cloud():
    text = " ".join(words)

    wordcloud = WordCloud(max_font_size=150, max_words=100,
                          background_color="white", mask=vbo_mask, min_font_size=5,
                          contour_width=1).generate(text)
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show(block=True)

generate_word_cloud()


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [unicode_tr(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)


for intent in intents["intents"]:
    """
    Tokenize etmek, cümleleri kelimelere ayırmak demektir.

    """
    for pattern in intent["patterns"]:
        # tokenize each word
        w = nltk.word_tokenize(metin_onisle(pattern))
        words.extend(w)
        # add documents in the corpus
        documents_X.append((w, intent["tag"]))
        # add to our classes list
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# stem and lower each word and remove duplicates
words = [unicode_tr(w.lower()) for w in words if w not in ignore_letters]

sw = stopwords.words('turkish')
words = [w for w in words if not w in sw]

words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))

# veri setini eğitme
training = []
output_empty = [0] * len(classes)

for doc in documents_X:
    bag = []
    pattern_words = doc[0]
    # unicode ile türkçe karakterleri düzeltme
    pattern_words = [unicode_tr(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])


training = np.array(training)
train_x = list(training[:, 0])
train_y = list(training[:, 1])

len(train_x[0]), len(train_y[0]), len(train_x), len(train_y),len(training)



model = Sequential()
model.add(Dense(200, input_shape=(len(train_x[0]),), activation="relu"))

model.add(Dense(150, activation="relu"))

model.add(Dense(len(train_y[0]), activation="softmax"))
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=500, batch_size=5, verbose=0)
model.save("chatbot_model.h5")

print("model created")

"""
# FOR MODEL EVALUATION

from sklearn.model_selection import train_test_split

from keras.callbacks import EarlyStopping

X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(200, input_shape=(len(X_train[0]),), activation='relu'))
model.add(Dense(150, activation="relu"))
model.add(Dense(len(y_train[0]), activation='softmax'))

# Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
# sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss="categorical_crossentropy", optimizer='adam' ,metrics=[tensorflow.keras.metrics.Precision()])

hist = model.fit(np.array(X_train), np.array(y_train), 
                epochs=500, batch_size=5, verbose=0, 
                validation_data=(np.array(X_test), np.array(y_test)),
                callbacks=[EarlyStopping(monitor='val_loss', patience=10, min_delta=0.0001)])

model.save("chatbot_model.h5")"""
print("model created")

# hyper parameters tuning



# modeli test etme
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score
preds = model.predict(np.array(X_test))
preds = np.argmax(preds, axis=1)
y_test = np.argmax(y_test, axis=1)
print(classification_report(y_test, preds))


# cross validation
def cross_validation():
    scores = model.evaluate(np.array(train_x), np.array(train_y), verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))


cross_validation()

model.summary()

# train-test accuracy graph
import matplotlib.pyplot as plt
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show(block=True)

# train-test loss graph
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show(block=True)



#########################################
#########################################


def chat():
    print("Benimle konuşabilirsin (Çıkmak için çıkış yazın.)")
    while True:
        inp = input("M.V.K.BOT: ")
        if inp.lower() == "çıkış":
            break

        results = model.predict(np.array([bag_of_words(metin_onisle(inp), words)]))[0]
        results_index = np.argmax(results)
        tag = classes[results_index]

        if results[results_index] > 0.7:
            for tg in intents["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            print(random.choice(responses))
        else:
            print(
                "Tam anlayamadım. Kendimi geliştirmek için çalışmaya devam edeceğim 😔 Daha açıklayıcı bir şekilde sorabilir misin?")


chat()


####


