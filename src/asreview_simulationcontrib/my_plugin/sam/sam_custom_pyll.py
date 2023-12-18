"""
just for illustration of what a plugin should look like
"""


import hyperopt


def sam_custom_pyll():
    return {
        "abbr": "sam-custom",
        "params": {
            "pct_excluded": hyperopt.hp.uniformint("pct_excluded", 0, 100),
            "pct_included": hyperopt.hp.uniformint("pct_included", 0, 100),
        },
    }
