import click
from asreviewcontrib.simulation.api import OneModelConfig
from asreviewcontrib.simulation.api.extending import dont_reassign_ofn_msg
from asreviewcontrib.simulation.api.extending import epilog
from asreview_simulationcontrib.my_plugin.ofn.ofn_custom_params import ofn_custom_params


default_params = ofn_custom_params()
name = "ofn-custom"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use an objective function from a plugin.",
    name=name,
    short_help="Custom ofn model from asreview-simulation-my-plugin",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'ofn' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--param_1",
    "param_1",
    default=default_params["param_1"],
    help="Parameter 1",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--param_2",
    "param_2",
    default=default_params["param_2"],
    help="Include this flag to turn on parameter 2",
    is_flag=True,
)
@click.pass_obj
def ofn_custom_subcommand(obj, force, param_1, param_2):
    if not force:
        assert obj.provided.ofn is False, dont_reassign_ofn_msg
    params = {
        "param_1": param_1,
        "param_2": param_2,
    }
    obj.config.ofn = OneModelConfig(abbr=name, params=params)
    obj.provided.ofn = True
