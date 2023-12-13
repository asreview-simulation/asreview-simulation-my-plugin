"""
This subcommand is for illustrating what an stp plugin should look like
"""
import click
from asreviewcontrib.simulation.api import OneModelConfig
from asreviewcontrib.simulation.api.extending import dont_reassign_stp_msg
from asreviewcontrib.simulation.api.extending import epilog
from asreview_simulationcontrib.my_plugin.stp.stp_custom_params import stp_custom_params


default_params = stp_custom_params()
name = "stp-custom"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a stopping model from a plugin.",
    name=name,
    short_help="Custom stp model from asreview-simulation-my-plugin",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'stp' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--pct",
    "pct",
    default=default_params["pct"],
    help="Only assess 'pct' percent of the data.",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def stp_custom_subcommand(obj, force, pct):
    if not force:
        assert obj.provided.stp is False, dont_reassign_stp_msg
    params = {
        "pct": pct,
    }
    obj.config.stp = OneModelConfig(abbr=name, params=params)
    obj.provided.stp = True
