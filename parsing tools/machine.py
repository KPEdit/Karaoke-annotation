# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
# from keras.optimizers import SGD
# from keras.layers.advanced_activations import LeakyReLU

# from sklearn.linear_model import SGDRegressor
# from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor , RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
# import sklearn as sk

import librosa as lb
import os
import pickle
from options import *

def open_mp3(path):
    y, sr = lb.load(path)
    x = lb.resample(y, sr, SAMPLE_RATE)
    x_stft = lb.stft(x)
    return x

def filt(data):
    add = []
    for d in data:
        text = d['text'].lower()
        if not ((text[0] == text[-1] and text[0] in "*\"'") or \
        (text[0] in "[{" and text[-1] in "]}")):
            # add.append([text, d["start"], d['duration']])
            add.append(d)
    return add

def gen_sets():
    musics = os.listdir(RAW_DATA_DIR)
    subs = os.listdir(RAW_SUBT_DIR)
    x_set = []
    y_set = []
    for i in range(len(musics)):
        x_set.append(open_mp3(os.path.join(RAW_DATA_DIR, musics[i])))
        with open(os.path.join(RAW_SUBT_DIR, subs[i]), 'rb') as inp:
            data = pickle.load(inp)
            add = filt(data)
            y_set.append(add)

    return x_set, y_set



if __name__ == '__main__':
    # r = readSubs()
    # for i in r:
    #     x_train, y_train = split_data(i)

    # subts = os.listdir(RAW_SUBT_DIR)
    # path = os.path.join(RAW_SUBT_DIR, subts[1])
    # i = readSub(path)
    # x_train, y_train = split_data(i)
    # print(x_train)
    # print(y_train)

    musics = os.listdir(RAW_DATA_DIR)
    subs = os.listdir(RAW_SUBT_DIR)
    x_set = []
    y_set = []
    i = 2
    x_set.append(open_mp3(os.path.join(RAW_DATA_DIR, musics[i])))
    with open(os.path.join(RAW_SUBT_DIR, subs[i]), 'rb') as inp:
        data = pickle.load(inp)
        add = filt(data)
        y_set.append(add)

    # print(x_set)
    # print(y_set)
    tfdf = TfidfVectorizer()
    a = []
    for w in y_set[0]:
        a.append(w['text'])
    td = tfdf.fit_transform(a)
    model = RandomForestRegressor()
    model.fit(x_set,td)
    # y_test = model.predict(x_set)
    # print(accuracy_score(td,y_test))

    # a = set()
    # c1 = 0
    # c2 = 0
    # musics = os.listdir(RAW_DATA_DIR)
    # for m in range(len(musics)):
    #     path = os.path.join(RAW_DATA_DIR, musics[m])
    #     sr = lb.get_samplerate(path)
    #     if sr == 44100:
    #         c1 += 1
    #     if sr == 48000:
    #         c2 += 1
    # print(a)
    # print(c1, c2)
















#
