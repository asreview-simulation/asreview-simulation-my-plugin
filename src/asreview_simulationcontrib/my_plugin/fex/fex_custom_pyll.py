"""
Same as fex-tfidf from asreview-simulation, just for illustration of what a plugin should look like
"""
import hyperopt


def fex_custom_pyll():
    return {
        "abbr": "fex-custom",
        "params": {
            "ngram_max": hyperopt.hp.choice("ngram_max", range(1, 4, 1)),
            "split_ta": hyperopt.hp.choice("split_ta", [True, False]),
            "stop_words": hyperopt.hp.choice("stop_words", ["english", "none"]),
            "use_keywords": hyperopt.hp.choice("use_keywords", [True, False]),
        },
    }
