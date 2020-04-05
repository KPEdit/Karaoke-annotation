from youtube_parser import readSub, readSubs
from pydub import AudioSegment
from options import *

import soundfile as sf
import librosa as lb
import numpy as np
import audioread
import random
import os


def genAudioPices(path):
    y, sr = lb.load(path)
    if sr != SAMPLE_RATE:
        y = lb.resample(y,sr,SAMPLE_RATE)
    step = SLICE_TIME * SAMPLE_RATE
    a = []
    for i in range(0,len(y),step):
        a.append(y[i:i+step])

def slice(path_in, path_out, **kwargs):
    sr = lb.get_samplerate(path_in)
    a,_ = lb.load(path_in, sr=sr, **kwargs)
    dur = lb.get_duration(a)

    name, form = os.path.basename(path_in).split('.')
    if form == 'mp3':
        form = 'wav'
    time = SLICE_TIME*sr
    n = int(dur/SLICE_TIME/2)
    for i in range(0, n):
        out = os.path.join(path_out, f"{name}_{SLICE_TIME}_{i}t{i+1}.{form}")
        b = np.asfortranarray([a[0][i*time:(i+1)*time],
                    a[1][i*time:(i+1)*time]])
        lb.output.write_wav(out,b,sr)
    out = os.path.join(path_out, f"{name}_{SLICE_TIME}_{n}t{n+1}.{form}")
    b = np.asfortranarray([a[0][n*time:],
                a[1][n*time:]])
    lb.output.write_wav(out,b,sr)

def main_slice():
    raw_audios = os.listdir(RAW_DATA_DIR)
    if PARSE_ALL:
        for audio_name in raw_audios:
            audio_root = os.path.join(RAW_DATA_DIR, audio_name)
            slice(audio_root, SLICED_DIR, mono=False)


if __name__ == '__main__':
    d = os.listdir(MY_MUSIC_DIR)
    for f in d:
        path = os.path.join(MY_MUSIC_DIR, f)
        a = genAudioPices(path)
        print(a)




























#
