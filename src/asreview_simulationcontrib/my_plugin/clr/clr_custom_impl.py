"""
Same as clr-nb from asreview-simulation, just an illustration of what a plugin should look like
"""
from asreview.models.classifiers.nb import NaiveBayesClassifier


def clr_custom_impl(params, _random_state):
    return NaiveBayesClassifier(**params)
