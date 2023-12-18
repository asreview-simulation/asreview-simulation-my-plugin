"""
This subcommand is just used for illustrating what a plugin should look like
"""
import click
from asreviewcontrib.simulation.api import OneModelConfig
from asreviewcontrib.simulation.api.extending import dont_reassign_sam_msg
from asreviewcontrib.simulation.api.extending import epilog
from asreview_simulationcontrib.my_plugin.sam.sam_custom_params import sam_custom_params


default_params = sam_custom_params()
abbr = "sam-custom"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a sampling model from a plugin.",
    name=abbr,
    short_help="Custom sam model from asreview-simulation-my-plugin",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'sam' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--pct_excluded",
    "pct_excluded",
    default=default_params["pct_excluded"],
    help="Use 'pct_excluded' percent of the irrelevant records as prior.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--pct_included",
    "pct_included",
    default=default_params["pct_included"],
    help="Use 'pct_included' percent of the relevant records as prior.",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def sam_custom_subcommand(obj, force, pct_excluded, pct_included):
    if not force:
        assert obj.provided.sam is False, dont_reassign_sam_msg
    params = {
        "pct_excluded": pct_excluded,
        "pct_included": pct_included,
    }
    obj.config.sam = OneModelConfig(abbr=abbr, params=params)
    obj.provided.sam = True
