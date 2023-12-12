from asreviewcontrib.simulation.api.extending import PluginQuad
from asreview_simulationcontrib.my_plugin.ofn.ofn_custom_impl import ofn_custom_impl
from asreview_simulationcontrib.my_plugin.ofn.ofn_custom_params import ofn_custom_params
from asreview_simulationcontrib.my_plugin.ofn.ofn_custom_pyll import ofn_custom_pyll
from asreview_simulationcontrib.my_plugin.ofn.ofn_custom_subcommand import ofn_custom_subcommand


ofn_custom_plugin_quad = PluginQuad(
    subcommand=ofn_custom_subcommand,
    default_params=ofn_custom_params,
    pyll=ofn_custom_pyll,
    impl=ofn_custom_impl
)
