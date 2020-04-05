# from youtube_parser import readSub, readSubs
# from pydub import AudioSegment
from options import *

import soundfile as sf
import librosa as lb
import numpy as np
import audioread
import random
import pickle
import os


def genAudioPices(path):
    y, sr = lb.load(path)
    if sr != SAMPLE_RATE:
        y = lb.resample(y,sr,SAMPLE_RATE)
    step = SLICE_TIME * SAMPLE_RATE
    x = []
    for i in range(0,len(y),step):
        x.append(y[i:i+step])
    print(len(x))
    return x

def genForY(path):
    data = None
    with open(path, 'rb') as inp:
        data = pickle.load(inp)

    end = data[-1]['end']
    frames = int(end+SLICE_TIME)//SLICE_TIME
    y = [None for i in range(0,frames)]
    for d in data:
        ln = d['end'] - d['start']
        if ln <= SLICE_TIME:
            try:
                index = int(d['start']) // SLICE_TIME

                if y[index] is None:
                    y[index] = []
                y[index].append(d['text'])
            except:
                print("Error index: ",index)
                print("start: ", d['start'])
                print("text: ", d['text'])
                print("end: ", d['end'])
                print("max time: ",data[-1]['end'])
    print(len(y))
    return y

def main():
    m = os.listdir(MY_MUSIC_DIR)
    s = os.listdir(MY_SUB_DIR)
    for f in range(0,len(m)):
        path_x = os.path.join(MY_MUSIC_DIR, m[f])
        path_y = os.path.join(MY_SUB_DIR, s[f])
        a = genAudioPices(path_x)
        b = genForY(path_y)
        # print(a[0].shape)

#
# def slice(path_in, path_out, **kwargs):
#     sr = lb.get_samplerate(path_in)
#     a,_ = lb.load(path_in, sr=sr, **kwargs)
#     dur = lb.get_duration(a)
#
#     name, form = os.path.basename(path_in).split('.')
#     if form == 'mp3':
#         form = 'wav'
#     time = SLICE_TIME*sr
#     n = int(dur/SLICE_TIME/2)
#     for i in range(0, n):
#         out = os.path.join(path_out, f"{name}_{SLICE_TIME}_{i}t{i+1}.{form}")
#         b = np.asfortranarray([a[0][i*time:(i+1)*time],
#                     a[1][i*time:(i+1)*time]])
#         lb.output.write_wav(out,b,sr)
#     out = os.path.join(path_out, f"{name}_{SLICE_TIME}_{n}t{n+1}.{form}")
#     b = np.asfortranarray([a[0][n*time:],
#                 a[1][n*time:]])
#     lb.output.write_wav(out,b,sr)
#
# def main_slice():
#     raw_audios = os.listdir(RAW_DATA_DIR)
#     if PARSE_ALL:
#         for audio_name in raw_audios:
#             audio_root = os.path.join(RAW_DATA_DIR, audio_name)
#             slice(audio_root, SLICED_DIR, mono=False)


if __name__ == '__main__':
    main()




























#
