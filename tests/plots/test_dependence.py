import matplotlib.pyplot as plt
import numpy as np
#matplotlib.use('Agg')
import shap

def test_random_dependence():
    fig, ax = plt.subplots(1, 1)
    shap.dependence_plot(0, np.random.randn(20, 5), np.random.randn(20, 5), show=False, ax=ax)

def test_random_dependence_no_interaction():
    fig, ax = plt.subplots(1, 1)
    shap.dependence_plot(0, np.random.randn(20, 5), np.random.randn(20, 5), show=False, interaction_index=None, ax=ax)