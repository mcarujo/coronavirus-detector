"""
This file is responsible to define the convolutional neural network that will be used as model, which is returned by a function.  
"""


from tensorflow.keras.layers import (Conv2D, Dense, Dropout, Flatten,
                                     MaxPooling2D)
from tensorflow.keras.models import Sequential


def cnn5_ann5_fibonacci_adam(IMG_FORMAT):
    model = Sequential()
    model.add(
        Conv2D(
            filters=8,
            kernel_size=(7, 7),
            padding="same",
            activation="relu",
            input_shape=IMG_FORMAT,
        )
    )
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Conv2D(filters=13, kernel_size=(3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=21, kernel_size=(3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=34, kernel_size=(3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=55, kernel_size=(3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(144, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model
