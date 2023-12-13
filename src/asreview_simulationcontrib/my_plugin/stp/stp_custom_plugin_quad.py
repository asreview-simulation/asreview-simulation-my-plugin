from asreviewcontrib.simulation.api.extending import PluginQuad
from asreview_simulationcontrib.my_plugin.stp.stp_custom_impl import stp_custom_impl
from asreview_simulationcontrib.my_plugin.stp.stp_custom_params import stp_custom_params
from asreview_simulationcontrib.my_plugin.stp.stp_custom_pyll import stp_custom_pyll
from asreview_simulationcontrib.my_plugin.stp.stp_custom_subcommand import stp_custom_subcommand


stp_custom_plugin_quad = PluginQuad(
    subcommand=stp_custom_subcommand,
    default_params=stp_custom_params,
    pyll=stp_custom_pyll,
    impl=stp_custom_impl
)
