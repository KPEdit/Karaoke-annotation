from slicer import getForXY
import librosa as lb
from librosa import display
import numpy as np
import matplotlib.pyplot as plt

def conver_audio_to_image(y):
    D = lb.stft(y, dtype=np.float32)
    DD = np.abs(D)
    # print(DD.shape)
    A = lb.amplitude_to_db(DD, ref=np.max)
    # print(A.shape)

def show_spect(DD):
    display.specshow(DD)
    plt.colorbar(format="%+2.0f dB")
    plt.tight_layout()
    plt.show()

def __load_gen():
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



if __name__ == '__main__':
    X, Y = __load_gen()
    conver_audio_to_image(X[0][40])





























#
