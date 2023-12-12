"""
This subcommand is basically the same as clr-nb from asreview-simulation,
it is just used for illustrating what a plugin should look like
"""
import click
from asreviewcontrib.simulation.api import OneModelConfig
from asreviewcontrib.simulation.api.extending import dont_reassign_clr_msg
from asreviewcontrib.simulation.api.extending import epilog
from asreview_simulationcontrib.my_plugin.clr.clr_custom_params import clr_custom_params


default_params = clr_custom_params()
name = "clr-custom"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a classifier from a plugin.",
    name=name,
    short_help="Custom clr model from asreview-simulation-my-plugin",
)
@click.option(
    "--alpha",
    "alpha",
    default=default_params["alpha"],
    help="Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'clr' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def clr_custom_subcommand(obj, alpha, force):
    if not force:
        assert obj.provided.clr is False, dont_reassign_clr_msg
    params = {
        "alpha": alpha,
    }
    obj.config.clr = OneModelConfig(abbr=name, params=params)
    obj.provided.clr = True
