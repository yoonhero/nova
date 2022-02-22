import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from utils import INPUT_SHAPE, batch_generator
import argparse
import os
import matplotlib.pyplot as plt


np.random.seed(0)


def load_data(args):
    data_df = pd.read_csv(os.path.join(os.getcwd(), args.data_dir, "driving_log.csv"), names=[
                          'center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed'])

    X = data_df[['center', 'left', 'right']].values
    y = data_df[['steering']].values

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=args.test_size, random_state=0)

    return X_train, X_valid, y_train, y_valid


def build_model(args):
    model = Sequential()
    model.add(Lambda(lambda x: x/127.5-1.0, input_shape=INPUT_SHAPE))
    model.add(Conv2D(24, (5, 5), activation='elu', strides=(2, 2)))
    model.add(Conv2D(36, (5, 5), activation='elu', strides=(2, 2)))
    model.add(Conv2D(48, (5, 5), activation='elu', strides=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='elu'))
    model.add(Conv2D(64, (3, 3), activation="elu"))
    model.add(Flatten())
    model.add(Dense(100, activation='elu'))
    model.add(Dense(50, activation='elu'))
    model.add(Dense(10, activation="elu"))
    model.add(Dense(1))
    model.summary()

    return model

def visualizeHistory(history):
    print(history)
    y_vloss = history.history["val_loss"]
    y_loss = history.history['loss']

    x_len = np.arange(len(y_loss))
    plt.plot(x_len, y_vloss, marker=".", c="red", label="Testset Loss")
    plt.plot(x_len, y_loss, marker=".", c="blue", label="Trainset loss")

    plt.legend(loc="upper right")
    
    plt.grid()
    plt.xlabel("epoch")
    plt.ylabel("loss")
    plt.show()

def train_model(model, args, X_train, X_valid, y_train, y_valid):
    checkpoint = ModelCheckpoint("model-{epoch:03d}.h5", monitor="val_loss",
                                 verbose=1, save_best_only=args.save_best_only, mode="auto")

    model.compile(loss="categorical_crossentropy",
                  metrics=['accuracy'],
                  optimizer="adam")

    train_data, train_labels = batch_generator(args.data_dir, X_train, y_train, args.batch_size, True)
    
    X_test, Y_test = batch_generator(args.data_dir, X_valid, y_valid, args.batch_size, False)
    
    print(Y_test)
    
    history = model.fit(
        train_data, train_labels,
        validation_data=(X_test, Y_test),
        callbacks=[checkpoint], 
        epochs=args.nb_epoch
    )
    
    print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))

    visualizeHistory(history)

def s2b(s):
    s = s.lower()

    return s == "true" or s == "yes" or s == "y" or s == "1"


def main():
    parser = argparse.ArgumentParser(
        description="Steering System on Simulation Test Program")

    parser.add_argument('-d', help='data directory',
                        dest='data_dir',          type=str,   default='data')
    parser.add_argument('-t', help='test size fraction',
                        dest='test_size',         type=float, default=0.2)
    parser.add_argument('-k', help='drop out probability',
                        dest='keep_prob',         type=float, default=0.5)
    parser.add_argument('-n', help='number of epochs',
                        dest='nb_epoch',          type=int,   default=30)
    parser.add_argument('-s', help='samples per epoch',
                        dest='samples_per_epoch', type=int,   default=20000)
    parser.add_argument('-b', help='batch size',
                        dest='batch_size',        type=int,   default=40)
    parser.add_argument('-o', help='save best models only',
                        dest='save_best_only',    type=s2b,   default='true')
    parser.add_argument('-l', help='learning rate',
                        dest='learning_rate',     type=float, default=1.0e-4)
    args = parser.parse_args()

    # print parameters
    print('-' * 30)
    print('Parameters')
    print('-' * 30)
    for key, value in vars(args).items():
        print('{:<20} := {}'.format(key, value))
    print('-' * 30)

    # load data
    data = load_data(args)
    # build model
    model = build_model(args)
    # train model on data, it saves as model.h5
    train_model(model, args, *data)


if __name__ == '__main__':
    main()
