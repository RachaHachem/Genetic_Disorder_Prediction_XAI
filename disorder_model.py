import os
from tensorflow.keras.models import load_model
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import logging
import numpy as np
import pickle
import matplotlib.pyplot as plt
import tensorflow
tensorflow.compat.v1.disable_v2_behavior()
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class DisorderPredictor:
    def __init__(self, model1_path, model2_path):
        logging.info("Predictor class initialized")
        self.disorder_model = load_model(model1_path)
        self.subclass_model = load_model(model2_path)
        logging.info("Model is loaded!")

    def process_input(self, ):  # add input features as parameters
        # normalize input
        # append to an array
        # return array
        return True

    def predict(self, ):  # add input features as parameters
        model_input = self.process_input()  # input_model is a normalized array of input
        disorder_prediction = self.disorder_model.predict(
            model_input)  # gives the disorder
        # append disorder_prediction to model_input array
        subclass_prediction = self.subclass_model.predict(
            model_input)  # gives subclass
        subclass = ''
        # reverse encoding -> return the subclass not encoded
        return subclass
