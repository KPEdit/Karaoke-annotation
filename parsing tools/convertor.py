import matplotlib.pyplot as plt
import librosa.display
import librosa as lb
import numpy as np
import options
import random
import os

random.seed(40)

sliced_list = os.listdir(options.SLICED_DIR)
items = random.choices(sliced_list, k = 3)

y = []
for item in items:
    path = os.path.join(options.SLICED_DIR, item)
    sr = lb.get_samplerate(path)
    a = lb.load(path, sr=None)
    y.append(a)

def harm_perc_save():
    for i in range(0,len(items)):
        out = os.path.join(options.DATA_DIR,"Experiment")
        name = items[i]
        names = name.split('.')
        y_harmonic, y_percussive = librosa.effects.hpss(y[i][0])
        out_1 = out + f"\\{names[0]}_percussive.{names[1]}"
        lb.output.write_wav(out_1,y_percussive,y[i][1])
        out_1 = out + f"\\{names[0]}_harmonic.{names[1]}"
        lb.output.write_wav(out_1,y_harmonic,y[i][1])

def magphase_scale_save():
    for i in range(0,len(items)):
        out = os.path.join(options.DATA_DIR,"Experiment")
        name = items[i]
        names = name.split('.')
        S_full, phase = librosa.magphase(librosa.stft(y[i][0]))
        S_filter = librosa.decompose.nn_filter(S_full,
                                       aggregate=np.median,
                                       metric='cosine',
                                       width=int(librosa.time_to_frames(2, sr=y[i][1])))

        out_1 = out + f"\\{names[0]}_raw_filter.{names[1]}"
        lb.output.write_wav(out_1,lb.istft(S_filter),y[i][1])
        S_filter = np.minimum(S_full, S_filter)
        out_1 = out + f"\\{names[0]}_min_filter.{names[1]}"
        lb.output.write_wav(out_1,lb.istft(S_filter),y[i][1])

        margin_i, margin_v = 2, 10
        power = 2

        mask_i = librosa.util.softmask(S_filter,
                               margin_i * (S_full - S_filter),
                               power=power)

        mask_v = librosa.util.softmask(S_full - S_filter,
                               margin_v * S_filter,
                               power=power)

        S_foreground = mask_v * S_full
        S_background = mask_i * S_full

        ISF = lb.istft(S_foreground)

        out_1 = out + f"\\{names[0]}_S_foreground.{names[1]}"
        lb.output.write_wav(out_1,ISF,y[i][1])
        print(ISF)
# S_foreground

if __name__ == '__main__':
    magphase_scale_save()

































#
