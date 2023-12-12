"""
Same as qry-max-random from asreview-simulation, just an illustration of what a plugin should look like
"""
from asreview.models.query.mixed import MixedQuery


def qry_custom_impl(params, random_state):
    mapped_params = {
        "strategy_1": "max",
        "strategy_2": "random",
        "mix_ratio": params["fraction_max"],
    }
    return MixedQuery(**mapped_params, random_state=random_state)
