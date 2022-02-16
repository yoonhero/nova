import numpy as np
import matploblib.pyplot as plt
import keras
from keras import layers
from keras.models import Model
from sklearn.utils import shuffle
from skleran.model_selection import train_test_split
from imgaug import augmenters as iaa

import random


seq = iaa.Sequntial([
    iaa.GaussianBlur(sigma=(0, 0.5)),
    iaa.Affine(
        scale={"x":(0.9, 1.1), "y": (0.9, 1.1)},
        translate_percent={"x":(-0.1, 0.1), "y": (-0.1, 0.1)},
        rotate=(-30, 30),
        order=[0, 1],
        cval=255
        )
], random_order=True)

augs = seq.augment_images(augs)


