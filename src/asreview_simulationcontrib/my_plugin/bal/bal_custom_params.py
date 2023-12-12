"""
Same as bal-double from asreview-simulation (but with slightly different defaults),
just for illustration of what a plugin should look like
"""


def bal_custom_params():
    return {
        "a": 2.154,
        "alpha": 0.93,
        "b": 0.788,
        "beta": 0.99,
    }
