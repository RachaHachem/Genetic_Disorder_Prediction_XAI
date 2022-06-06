from tensorflow.keras.models import load_model
import numpy as np
import os
import logging
import tensorflow
tensorflow.compat.v1.disable_v2_behavior()


# tensorflow.compat.v1.disable_eager_execution()


# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class DisorderPredictor:
    def __init__(self, model1_path, model2_path):
        logging.info("Predictor class initialized")
        self.disorder_model = load_model(model1_path)
        # self.disorder_model._make_predict_function()
        self.subclass_model = load_model(model2_path)
        # self.subclass_model._make_predict_function()

        logging.info("Model is loaded!")

    def process_input(self, input):
        # normalize input
        max = np.array([14.000000, 5.609829, 51.000000, 64.000000, 4.000000, 12.000000, 1.000000, 1.000000,
                        1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 2.000000, 1.000000, 1.000000, 1.000000,
                        1.000000, 1.000000, 3.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000])
        for i in range(len(max)):
            logging.info("before: ", input[i])
            input[i] = input[i].astype('float')/max[i].astype('float')
            logging.info("after: ", input[i])
        return input

    def predict(self, explainer, age, bcc, mother_age, father_age, abortions, wbcc, mother_gene,
                father_gene, maternal_gene, paternal_gene, status, rr, hr, risk, gender, folic_acid, maternal_illness,
                conceptive, anomalies, defects, blood_test, symptom1, symptom2, symptom3, symptom4, symptom5):

        input = np.array([age, bcc, mother_age, father_age, abortions, wbcc, mother_gene,
                          father_gene, maternal_gene, paternal_gene, status, rr, hr, risk, gender, folic_acid, maternal_illness,
                          conceptive, anomalies, defects, blood_test, symptom1, symptom2, symptom3, symptom4, symptom5])

        # model_input is a normalized array of input
        model_input = self.process_input(input)

        model_input = np.reshape(model_input, (1, 26))

        genetic_explainer = explainer.plot_explainer(
            self.disorder_model, model_input, 'genetic')

        disorder_prediction = self.disorder_model.predict(model_input)
        disorder_prediction = disorder_prediction.argmax()

        disorder_prediction = disorder_prediction.astype('float')/2

        # append disorder_prediction to model_input array
        model_input = np.append(model_input, disorder_prediction)

        model_input = np.reshape(model_input, (1, 27))

        subclass_explainer = explainer.plot_explainer(
            self.subclass_model, model_input, 'subclass')

        subclass_prediction = self.subclass_model.predict(model_input).argmax()

        # reverse encoding -> return the subclass not encoded
        subclass = ''
        if subclass_prediction == 0:
            subclass = "Alzheimer's"
        elif subclass_prediction == 1:
            subclass = "Cancer"
        elif subclass_prediction == 2:
            subclass = "Cystic fibrosis"
        elif subclass_prediction == 3:
            subclass = "Diabetes"
        elif subclass_prediction == 4:
            subclass = "Hemochromatosis"
        elif subclass_prediction == 5:
            subclass = "Leber's hereditary optic neuropathy"
        elif subclass_prediction == 6:
            subclass = "Leigh syndrome"
        elif subclass_prediction == 7:
            subclass = "Mitochondrial myopathy"
        elif subclass_prediction == 8:
            subclass = "Tay-Sachs"

        return [subclass, genetic_explainer, subclass_explainer]
        # return subclass
