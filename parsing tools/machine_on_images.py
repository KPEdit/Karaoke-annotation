import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Activation
from keras.optimizers import SGD
from keras.layers.advanced_activations import LeakyReLU
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from machine_preprocessing import load_images, getY
import numpy as np

x_train = load_images()
y_train, output_shape = getY()

img_width = 389
img_height = 515
img_chanels = 3

nb_train_samples = 82
epochs = 10
batch_size = 8

if K.image_data_format() == 'channels_first':
    input_shape = (img_chanels, img_width, img_height)
else:
    input_shape = (img_width, img_height, img_chanels)

model = Sequential()
model.add(Conv2D(32, (2,2), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (2,2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (2,2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(.3))
model.add(Dense(output_shape, activation='softmax'))

model.compile(loss='categorical_crossentropy',
            optimizer='rmsprop',
            metrics=['accuracy'])

# print(len(x_train[2][3][1]))
x_train = np.array(x_train)
y_train = np.array(y_train)
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)

loss, acc = model.evaluate(x_train, y_train)
print(acc*100)

# print(y_train)
# print(len(y_train), len(x_train))















#
