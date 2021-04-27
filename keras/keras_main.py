from keras.datasets import cifar10
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import tensorflow as tf

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sess = len(tf.config.experimental.list_physical_devices('GPU'))
    print(sess)

    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    model = Sequential()
    # 32 Filter - 3x3
    model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(32, 32, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))

    model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

    X_train = X_train.astype(np.float32) / 255.
    X_test = X_test.astype(np.float32) / 255.
    y_train = y_train == 1
    y_test = y_test == 1

    # Klasse 1 = Auto
    model.fit(X_train, y_train == 1, batch_size=128, epochs=10, shuffle=True)
    train_evaluate = model.evaluate(X_train, y_train)
    test_evaluate = model.evaluate(X_test, y_test)

    print(train_evaluate)
    print(test_evaluate)

    model.save('weights.h5', save_format='h5')
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
