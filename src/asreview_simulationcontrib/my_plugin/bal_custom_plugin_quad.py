from asreviewcontrib.simulation.api.extending import PluginQuad
from asreview_simulationcontrib.my_plugin.bal_custom_impl import bal_custom_impl
from asreview_simulationcontrib.my_plugin.bal_custom_params import bal_custom_params
from asreview_simulationcontrib.my_plugin.bal_custom_pyll import bal_custom_pyll
from asreview_simulationcontrib.my_plugin.bal_custom_subcommand import bal_custom_subcommand


bal_custom_plugin_quad = PluginQuad(
    subcommand=bal_custom_subcommand,
    default_params=bal_custom_params,
    pyll=bal_custom_pyll,
    impl=bal_custom_impl
)
