"""
Same as fex-tfidf from asreview-simulation (but with slightly different defaults),
just for illustration of what a plugin should look like
"""
from typing import Any
from typing import Dict


def fex_custom_params() -> Dict[str, Any]:
    return {
        "ngram_max": 2,
        "split_ta": False,
        "stop_words": "english",
        "use_keywords": False,
    }
