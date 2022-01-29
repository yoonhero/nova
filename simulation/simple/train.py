import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from utils import INPUT_SHAPE, batch_generator
import argparse
import os



np.random.seed(0)


def load_data(args):
    data_df = pd.read_csv(os.path.join(args.data_dir, 'driving_log.csv'))

    X = data_df[['center', 'left', 'right']].values
    y = data_df['steering'].values
    
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=args.test_size, random_state=0)

    return X_train, X_valid, y_train, y_valid

def build_model(args):
    model = Sequential()
    model.add(Lambda(lambda x: x/127.5-1.0, input_shape=INPUT_SHAPE))
    model.add(Conv2D(24, 5, 5, activation='elu', subsample=(2,2)))
    model.add(Conv2D(36, 5, 5, activation='elu', subsample=(2,2)))
    model.add(Conv2D(48, 5, 5, activation="elu"))
    model.add(Conv2D(64, 3, 3, activation="elu"))
    model.add(Conv2D(64, 3,3,activation="elu"))
    model.add(Dropout(args.keep_prob))
    model.add(Flatten())
    model.add(Dense(100, activation="elu"))
    model.add(Dense(50, activation='elu'))
    model.add(Dense(10, activation="elu"))
    model.add(Dense(1))
    model.summary()

    return model