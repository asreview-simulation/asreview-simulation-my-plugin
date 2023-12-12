"""
This subcommand is basically the same as bal-double from asreview-simulation,
it is just used for illustrating what a plugin should look like
"""
import click
from asreviewcontrib.simulation.api import OneModelConfig
from asreviewcontrib.simulation.api.extending import dont_reassign_bal_msg
from asreviewcontrib.simulation.api.extending import epilog
from asreview_simulationcontrib.my_plugin.bal.bal_custom_params import bal_custom_params


default_params = bal_custom_params()
name = "bal-custom"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a balancer from a plugin.",
    name=name,
    short_help="Custom bal model from asreview-simulation-my-plugin",
)
@click.option(
    "--a",
    "a",
    default=default_params["a"],
    help="Weight of the 1's. Higher values mean linearly more 1's in your training sample.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--alpha",
    "alpha",
    default=default_params["alpha"],
    help="Scaling of the weight of the 1's, as a function of the ratio of ones to zeros. "
    + "A positive value means that the lower the ratio of zeros to ones, the higher "
    + "the weight of the ones.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--b",
    "b",
    default=default_params["b"],
    help="How strongly we want to sample depending on the total number of samples. A value "
    + "of 1 means no dependence on the total number of samples, while lower "
    + "values mean increasingly stronger dependence on the number of samples.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--beta",
    "beta",
    default=default_params["beta"],
    help="Scaling of the weight of the zeros depending on the number of samples. Higher "
    + "values means that larger samples are more strongly penalizing zeros.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'bal' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def bal_custom_subcommand(obj, a, alpha, b, beta, force):
    if not force:
        assert obj.provided.bal is False, dont_reassign_bal_msg
    params = {
        "a": a,
        "alpha": alpha,
        "b": b,
        "beta": beta,
    }
    obj.config.bal = OneModelConfig(abbr=name, params=params)
    obj.provided.bal = True
