from google.cloud import aiplatform
import numpy as np
import pathlib
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers


model = keras._load("gs://my-kubernetes-codelab-342121-bucket/mpg/model")

model.summary()