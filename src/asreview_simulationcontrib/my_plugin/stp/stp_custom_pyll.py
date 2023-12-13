"""
just for illustration of what a plugin should look like
"""


import hyperopt


def stp_custom_pyll():
    return {
        "abbr": "stp-custom",
        "params": {
            "pct": hyperopt.hp.uniformint("pct", 0, 100),
        },
    }
