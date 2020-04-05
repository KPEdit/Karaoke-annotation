import speech_recognition as srr
import os
import numpy as np
import soundfile as sf
from options import *
from scipy.io import wavfile

r = srr.Recognizer()
# musics = os.listdir(RAW_DATA_DIR)
# i = 1
# path = os.path.join(RAW_DATA_DIR, musics[i])
# # data, sr = lb.load(path)
# data, sr = sf.read("new.wav")
# y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)
#
# wavfile.write("new.wav",sr, y)
audio = srr.AudioFile('new.wav')

with audio as s:
    # print(s)
    b = r.record(s)
    a = r.recognize_google(b, language="ru-RU")
    print(a)
