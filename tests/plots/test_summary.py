import warnings

import matplotlib.pyplot as plt
import numpy as np
import pytest

import shap


@pytest.mark.mpl_image_compare
def test_random_summary():
    """ Just make sure the summary_plot function doesn't crash.
    """
    np.random.seed(0)
    fig, ax = plt.subplots(1, 1)
    shap.summary_plot(np.random.randn(20, 5), show=False, ax=ax)
    plt.tight_layout()
    return fig


@pytest.mark.mpl_image_compare
def test_random_summary_with_data():
    """ Just make sure the summary_plot function doesn't crash with data.
    """
    np.random.seed(0)
    fig, ax = plt.subplots(1, 1)
    shap.summary_plot(np.random.randn(20, 5), np.random.randn(20, 5), show=False, ax=ax)
    plt.tight_layout()
    return fig


@pytest.mark.mpl_image_compare
def test_random_multi_class_summary():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 1)
    shap.summary_plot([np.random.randn(20, 5) for i in range(3)], np.random.randn(20, 5), show=False, ax=ax)
    plt.tight_layout()
    return fig


@pytest.mark.mpl_image_compare
def test_random_summary_bar_with_data():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 1)
    shap.summary_plot(np.random.randn(20, 5), np.random.randn(20, 5), plot_type="bar", show=False, ax=ax)
    plt.tight_layout()
    return fig


@pytest.mark.mpl_image_compare
def test_random_summary_dot_with_data():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 1)
    shap.summary_plot(np.random.randn(20, 5), np.random.randn(20, 5), plot_type="dot", show=False, ax=ax)
    plt.tight_layout()
    return fig


@pytest.mark.mpl_image_compare
def test_random_summary_violin_with_data():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 1)
    shap.summary_plot(np.random.randn(20, 5), np.random.randn(20, 5), plot_type="violin", show=False, ax=ax)
    plt.tight_layout()
    return fig


@pytest.mark.mpl_image_compare
def test_random_summary_layered_violin_with_data():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 1)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        shap.summary_plot(np.random.randn(20, 5), np.random.randn(20, 5), plot_type="layered_violin", show=False, ax=ax)
    plt.tight_layout()
    return fig


@pytest.mark.mpl_image_compare
def test_random_summary_with_log_scale():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 1)
    shap.summary_plot(np.random.randn(20, 5), use_log_scale=True, show=False, ax=ax)
    plt.tight_layout()
    return fig
