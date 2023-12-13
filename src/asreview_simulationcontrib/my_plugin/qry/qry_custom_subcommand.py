"""
This subcommand is basically the same as qry-max-random from asreview-simulation,
it is just used for illustrating what a plugin should look like
"""
import click
from asreviewcontrib.simulation.api import OneModelConfig
from asreviewcontrib.simulation.api.extending import dont_reassign_qry_msg
from asreviewcontrib.simulation.api.extending import epilog
from asreview_simulationcontrib.my_plugin.qry.qry_custom_params import qry_custom_params


default_params = qry_custom_params()
abbr = "qry-custom"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a query model from a plugin.",
    name=abbr,
    short_help="Custom qry model from asreview-simulation-my-plugin",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'qry' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--fraction_max",
    "fraction_max",
    default=default_params["fraction_max"],
    help="Fraction of mixture that is queried using the Max strategy",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--n_instances",
    "n_instances",
    default=default_params["n_instances"],
    help="Number of records per query",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def qry_custom_subcommand(obj, force, fraction_max, n_instances):
    if not force:
        assert obj.provided.qry is False, dont_reassign_qry_msg
    params = {
        "fraction_max": fraction_max,
        "n_instances": n_instances,
    }
    obj.config.qry = OneModelConfig(abbr=abbr, params=params)
    obj.provided.qry = True
