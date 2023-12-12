from asreviewcontrib.simulation.api.extending import PluginQuad
from asreview_simulationcontrib.my_plugin.clr.clr_custom_impl import clr_custom_impl
from asreview_simulationcontrib.my_plugin.clr.clr_custom_params import clr_custom_params
from asreview_simulationcontrib.my_plugin.clr.clr_custom_pyll import clr_custom_pyll
from asreview_simulationcontrib.my_plugin.clr.clr_custom_subcommand import clr_custom_subcommand


clr_custom_plugin_quad = PluginQuad(
    subcommand=clr_custom_subcommand,
    default_params=clr_custom_params,
    pyll=clr_custom_pyll,
    impl=clr_custom_impl
)
