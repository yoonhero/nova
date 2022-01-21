import cv2
import numpy as np
import glob
import sys
import time
import os
from sklearn.model_selection import train_test_split


class NeuralNetwork(object):
    def __init__(self):
        self.model = None

    def create(self, layer_sizes):
        self.model = cv2.ml.ANN_MLP_create()
        self.model.setLayerSizes(np.int32(layer_sizes))
        self.model.setTrainMethod(cv2.ml.ANN_MLP_BACKDROP)
        self.model.setActivationFunctino(cv2.ml.ANN_MLP_SIGMOID, 2, 1)
        self.model.setTermCriteria((cv2.TERM_CRITERIA_COUNT, 100, 0.01))

    def train(self, X, y):
        start = time.time()

        print("Training...")
        self.model.train(np.float32(X), cv2.ml.ROW_SAMPLE, np.float32(y))

        end = time.time()
        print(f"Print Duration: {int(end - start)}s")

    def evaluate(self, X, y):
        ret, resp = self.model.predict(X)
        prediction = resp.argmax(-1)
        true_labels = y.argmax(-1)
        accuracy = np.mean(prediction == true_labels)
        return accuracy

    def save_model(self, path):
        directory = "saved_model"
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.model.save(path)
        print("Model saved to: " + "'" + path + "'")

    def load_model(self, path):
        if not os.path.exists(path):
            print("Model does not exist, exit")
            sys.exit()
        self.model = cv2.ml.ANN_MLP_load(path)

    def predict(self, X):
        resp = None
        try:
            ret, resp = self.model.predict(X)
            print("Prediction Result: ", ret, resp)
        except Exception as e:
            print(e)
        return resp.argmax(-1)
