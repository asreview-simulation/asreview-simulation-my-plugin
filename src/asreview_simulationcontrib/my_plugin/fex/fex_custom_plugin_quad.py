from asreviewcontrib.simulation.api.extending import PluginQuad
from asreview_simulationcontrib.my_plugin.fex.fex_custom_impl import fex_custom_impl
from asreview_simulationcontrib.my_plugin.fex.fex_custom_params import fex_custom_params
from asreview_simulationcontrib.my_plugin.fex.fex_custom_pyll import fex_custom_pyll
from asreview_simulationcontrib.my_plugin.fex.fex_custom_subcommand import fex_custom_subcommand


fex_custom_plugin_quad = PluginQuad(
    subcommand=fex_custom_subcommand,
    default_params=fex_custom_params,
    pyll=fex_custom_pyll,
    impl=fex_custom_impl
)
