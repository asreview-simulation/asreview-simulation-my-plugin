"""
Same as clr-nb from asreview-simulation, just for illustration of what a plugin should look like
"""
import hyperopt


def clr_custom_pyll():
    return {
        "abbr": "clr-custom",
        "params": {
            "alpha": hyperopt.hp.lognormal("alpha", 0, 1),
        },
    }
