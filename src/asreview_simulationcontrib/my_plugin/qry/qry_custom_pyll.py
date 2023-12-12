"""
Similar to qry-max-random from asreview-simulation, just for illustration of what a plugin should look like
"""
import hyperopt


def qry_custom_pyll():
    return {
        "abbr": "qry-custom",
        "params": {
            "fraction_max": hyperopt.hp.choice("fraction_max", [0.85, 0.90, 0.95]),
            "n_instances": hyperopt.hp.choice("n_instances", range(1, 100, 1)),
        },
    }
