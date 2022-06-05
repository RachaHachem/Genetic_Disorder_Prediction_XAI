import pickle
import matplotlib.pyplot as plt
import sklearn
import lifelines
import shap
import numpy as np


class Explainer:
    def __init__(self, path1, path2):
        with open(path1, 'rb') as f:
            self.genetic_data = pickle.load(f)
        with open(path2, 'rb') as f:
            self.subclass_data = pickle.load(f)

    def plot_explainer(self, model, input, data):
        if data == 'genetic':
            e = shap.DeepExplainer(model,  self.genetic_data)
        else:
            e = shap.DeepExplainer(model,  self.subclass_data)
        vals = e.shap_values(input)
        shap.initjs()
        features_importance = shap.force_plot(
            e.expected_value[0], vals[0], input, show=False)
        shap_html = f"<p>{features_importance.html()}</p>"
        return shap_html
