from asreviewcontrib.simulation.api.extending import PluginQuad
from asreview_simulationcontrib.my_plugin.ofn_custom_fun import ofn_plugin_fun
from asreview_simulationcontrib.my_plugin.ofn_custom_params import get_ofn_custom_params
from asreview_simulationcontrib.my_plugin.ofn_custom_pyll import ofn_custom_pyll
from asreview_simulationcontrib.my_plugin.ofn_custom_subcommand import ofn_custom_subcommand


ofn_custom_plugin_quad = PluginQuad(
    subcommand=ofn_custom_subcommand,
    default_params_getter=get_ofn_custom_params,
    pyll_getter=ofn_custom_pyll,
    impl=ofn_plugin_fun
)
