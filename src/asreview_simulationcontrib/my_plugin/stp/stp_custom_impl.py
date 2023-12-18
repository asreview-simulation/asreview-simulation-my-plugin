"""
just an illustration of what a plugin should look like
"""
from math import ceil
from asreview.data import ASReviewData
from asreviewcontrib.simulation.api import Config


def stp_custom_impl(config: Config, as_data: ASReviewData):
    # stopping model that stops after pct percent of the data
    pct = config.stp.params.get("pct")
    n_instances = config.qry.params.get("n_instances")
    if config.sam.abbr == "sam-handpicked":
        records = config.sam.params.get("records", None)
        rows = config.sam.params.get("rows", None)
        if rows is not None:
            n_remaining = len(as_data) - len(rows)
        elif records is not None:
            n_remaining = len(as_data) - len(records)
        else:
            raise ValueError("Neither rows or records have been defined.")
    elif config.sam.abbr == "sam-random":
        n_excluded = config.sam.params.get("n_excluded")
        n_included = config.sam.params.get("n_included")
        assert isinstance(n_excluded, int), "Expected n_excluded to be of type int"
        assert isinstance(n_included, int), "Expected n_included to be of type int"
        n_remaining = len(as_data) - n_excluded - n_included
    else:
        msg = f"Can't determine the number of prior samples for sampler '{config.sam.abbr}'" \
              + ", proceeding as if the number of remaining records is equal to all the records."
        print(msg)
        n_remaining = len(as_data)
    return int(ceil(pct * n_remaining / n_instances / 100))
