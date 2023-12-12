from asreviewcontrib.simulation.api.extending import PluginQuad
from asreview_simulationcontrib.my_plugin.qry.qry_custom_impl import qry_custom_impl
from asreview_simulationcontrib.my_plugin.qry.qry_custom_params import qry_custom_params
from asreview_simulationcontrib.my_plugin.qry.qry_custom_pyll import qry_custom_pyll
from asreview_simulationcontrib.my_plugin.qry.qry_custom_subcommand import qry_custom_subcommand


qry_custom_plugin_quad = PluginQuad(
    subcommand=qry_custom_subcommand,
    default_params=qry_custom_params,
    pyll=qry_custom_pyll,
    impl=qry_custom_impl
)
