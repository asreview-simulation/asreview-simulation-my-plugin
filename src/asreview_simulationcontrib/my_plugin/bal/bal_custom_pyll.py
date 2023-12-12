"""
Same as bal-double from asreview-simulation, just for illustration of what a plugin should look like
"""
import hyperopt


def bal_custom_pyll():
    return {
        "abbr": "bal-custom",
        "params": {
            "a": hyperopt.hp.lognormal("a", 0, 1),
            "alpha": hyperopt.hp.uniform("alpha", 0, 2),
            "b": hyperopt.hp.uniform("b", 0, 1),
            "beta": hyperopt.hp.uniform("beta", 0, 2),
        },
    }
