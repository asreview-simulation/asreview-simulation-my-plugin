"""
Same as bal-double from asreview-simulation, just an illustration of what a plugin should look like
"""
from asreview.models.balance.double import DoubleBalance


def bal_custom_impl(params, random_state):
    return DoubleBalance(**params, random_state=random_state)
