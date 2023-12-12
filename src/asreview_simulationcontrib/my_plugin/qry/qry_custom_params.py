"""
Same as qry-max-random from asreview-simulation (but with slightly different defaults),
just for illustration of what a plugin should look like
"""


def qry_custom_params():
    return {
        "fraction_max": 0.90,
        "n_instances": 1,
    }
