from slicer import getForXY
import librosa as lb
from librosa import display
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt
from options import SAMPLE_RATE, IMAGE_DIR

def conver_all_audio_to_image_func(func, y):
    x = []
    for audio in y:
        for ix in audio:
            x.append(func(ix))
    return x

def conver_audio_to_image_db(y):
    D = lb.stft(y)
    DD = np.abs(D)**2

    A = lb.amplitude_to_db(DD, ref=np.max)
    # print(A.shape)
    return A

def conver_audio_to_image_chroma(y):
    D = lb.stft(y)
    """POWER MAY BE OMITTED"""
    DD = np.abs(D)**2

    A = lb.feature.chroma_stft(S=DD, sr=SAMPLE_RATE)
    # print(A.shape)
    return A

def conver_audio_to_image_mel(y):
    D = lb.stft(y)
    """POWER MAY BE OMITTED"""
    DD = np.abs(D)**1

    A = lb.feature.melspectrogram(S=DD, sr=SAMPLE_RATE)
    # print(A.shape)
    return A

def save_all_mp3_as_img(data):
    for f in range(0, len(data)):
        save_mp3_as_img(data[f], str(f))

def save_mp3_as_img(data, index):
    display.specshow(data)
    plt.axis('off')
    plt.savefig(os.path.join(IMAGE_DIR, index)+".jpeg", bbox_inches='tight')
    plt.clf()

def load_images():
    files = os.listdir(IMAGE_DIR)
    x = []
    for f in files:
        img = Image.open(os.path.join(IMAGE_DIR, f))
        img_data = np.asarray(img)
        x.append(img_data)
    return x

def show_spect(DD):
    display.specshow(DD)
    plt.colorbar(format="%+2.0f dB")
    plt.tight_layout()
    plt.show()

def load_gen():
    """FUNCTION FOR THE DEVELOPER"""
    import pickle
    X, Y = None, None
    with open('X.xy', 'rb') as ooo:
        X = pickle.load(ooo)
    with open('Y.xy', 'rb') as ooo:
        Y = pickle.load(ooo)
    return X, Y

def __save_gen():
    """FUNCTION FOR THE DEVELOPER"""
    X, Y = getForXY()
    import pickle
    with open('X.xy', 'wb') as ooo:
        pickle.dump(X, ooo)
    with open('Y.xy', 'wb') as ooo:
        pickle.dump(Y, ooo)


def make1Darray(Y):
    y = []
    for i in Y:
        y += i
    return y

def num_to_word(y):
    m_set = set()
    m_set.add(None)
    for s in y:
        if s != None:
            for w in s:
                m_set.add(w)
    return m_set

def get_pre_fin_data(y,y_dic):
    pre_fin = []
    for s in y:
        if s == None:
            pre_fin.append((0,))
        else:
            # y_dic[s[0]]
            pre_fin.append(tuple([y_dic[i] for i in s]))
    return pre_fin


def normalize_Y(Y):
    offset = 1
    y = make1Darray(Y)
    yy = num_to_word(y)
    y_dic = {elem:(num+offset) for num,elem in enumerate(yy)}
    pre_fin = get_pre_fin_data(Y[0], y_dic)

    num_of_classes = len(yy)+1
    fin = np.zeros((len(y), num_of_classes))
    for i in range(0, len(pre_fin)):
        for j in range(0, len(pre_fin[i])):
            fin[i][pre_fin[i][j]] = 1
    # print(y)
    # print(fin[19])
    return fin, num_of_classes



def getY():
    _,Y = load_gen()
    return normalize_Y(Y)

if __name__ == '__main__':
    # X, Y = load_gen()
    # a = conver_audio_to_image_db(X[0][40])
        # b = conver_audio_to_image_db(X[0][40])
    # show_spect(b)
    # save_mp3_as_img(b, 'joi2')
        # a = conver_all_audio_to_image_func(conver_audio_to_image_db, X)
    # save_all_mp3_as_img(a)
        # x = load_images()
        # for ix in x:
        #     print(ix.shape)
    # print(len(a))
    # print(len(x))
    # print(Y[0])
    getY()































#
