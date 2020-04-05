# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
# from keras.optimizers import SGD
# from keras.layers.advanced_activations import LeakyReLU
#
# from sklearn.linear_model import SGDRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import VotingRegressor , RandomForestRegressor
# from sklearn.metrics import accuracy_score
# from sklearn.feature_extraction.text import TfidfVectorizer
# import sklearn as sk

import librosa as lb
import os
import pickle
from options import *




def gen_set(index):
    file = os.listdir(MY_SUB_DIR)[index]
    file_audio = os.listdir(MY_MUSIC_DIR)[index]
    path = os.path.join(MY_SUB_DIR, file)
    path_audio = os.path.join(MY_MUSIC_DIR, file_audio)
    y = []
    with open(path,'rb') as inp:
        y = pickle.load(inp)

    x, sr = lb.load(path_audio)
    x = lb.resample(x,sr,SAMPLE_RATE)
    return x,y

def gen_sets():
    pass

if __name__ == '__main__':
    x,y = gen_set(0)
    print(x.shape)



























#
