from asreviewcontrib.simulation.api.extending import PluginQuad
from asreview_simulationcontrib.my_plugin.sam.sam_custom_impl import sam_custom_impl
from asreview_simulationcontrib.my_plugin.sam.sam_custom_params import sam_custom_params
from asreview_simulationcontrib.my_plugin.sam.sam_custom_pyll import sam_custom_pyll
from asreview_simulationcontrib.my_plugin.sam.sam_custom_subcommand import sam_custom_subcommand


sam_custom_plugin_quad = PluginQuad(
    subcommand=sam_custom_subcommand,
    default_params=sam_custom_params,
    pyll=sam_custom_pyll,
    impl=sam_custom_impl
)
