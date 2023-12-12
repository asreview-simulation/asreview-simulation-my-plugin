"""
Same as fex-tfidf from asreview-simulation, just an illustration of what a plugin should look like
"""
from asreview.models.feature_extraction.tfidf import Tfidf


def fex_custom_impl(params, random_state):
    return Tfidf(**params, random_state=random_state)
