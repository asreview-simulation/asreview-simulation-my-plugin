"""
Same as fex-tfidf from asreview-simulation (but with slightly different defaults),
just for illustration of what a plugin should look like
"""


def fex_custom_params():
    return {
        "ngram_max": 2,
        "split_ta": False,
        "stop_words": "english",
        "use_keywords": False,
    }
