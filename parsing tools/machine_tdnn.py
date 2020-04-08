import dynastes
from dynastes.layers import TimeDelayLayer1D
import keras
from keras.models import Sequential
from keras.layers import Conv1D, Flatten, Input,Activation, Dense, Dropout, MaxPooling1D
from keras.optimizers import SGD
from keras.layers.advanced_activations import LeakyReLU


batch_size = 32
num_epochs = 5

model = Sequential()
input_shape = (1025, 188)

model.add(TimeDelayLayer1D(4, input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling1D(pool_size=2))

model.summary()

# X, Y = load_gen()
# # import numpy as np
# x = []
# for item in X[0]:
#     x.append(conver_audio_to_image_db(item))
# # x = np.array(x)
#
#
# model.fit(x,Y, batch_size=batch_size, verbose=1, nb_epoch=num_epochs)

# model.evaluate()




#
