"""
Just an illustration of what a plugin for a 'sam' model should look like
"""
from collections import Counter
from asreview.data import ASReviewData
from asreviewcontrib.simulation.api import Config


def sam_custom_impl(config: Config, as_data: ASReviewData):
    """Take a percentage of the relevant/irrelevant labeled records as priors"""
    prior_indices = list()
    pct_excluded = config.sam.params["pct_excluded"]
    pct_included = config.sam.params["pct_included"]

    counter = Counter(as_data.labels)
    n_irrelevant = counter[0]
    n_relevant = counter[1]

    n_prior_excluded = max(1, int(round(pct_excluded * n_irrelevant / 100)))
    n_prior_included = max(1, int(round(pct_included * n_relevant / 100)))

    seed = None

    return prior_indices, n_prior_included, n_prior_excluded, seed
