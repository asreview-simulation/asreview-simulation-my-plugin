"""
This subcommand is basically the same as fex-tfidf from asreview-simulation,
it is just used for illustrating what a plugin should look like
"""
import click
from asreviewcontrib.simulation.api import OneModelConfig
from asreviewcontrib.simulation.api.extending import dont_reassign_fex_msg
from asreviewcontrib.simulation.api.extending import epilog
from asreview_simulationcontrib.my_plugin.fex.fex_custom_params import fex_custom_params


default_params = fex_custom_params()
name = "fex-custom"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a feature extractor from a plugin.",
    name=name,
    short_help="Custom fex model from asreview-simulation-my-plugin",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'fex' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--ngram_max",
    "ngram_max",
    default=default_params["ngram_max"],
    help="Use n-grams up to ngram_max. For example in the case of ngram_max=2, monograms and bigrams could be used.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--split_ta",
    "split_ta",
    default=default_params["split_ta"],
    help="Include this flag to split ta.",
    is_flag=True,
)
@click.option(
    "--stop_words",
    "stop_words",
    default=default_params["stop_words"],
    help="When set to 'english', use stopwords. If set to 'none', do not use stop words.",
    show_default=True,
    type=click.Choice(["english", "none"]),
)
@click.option(
    "--use_keywords",
    "use_keywords",
    default=default_params["use_keywords"],
    help="Include this flag to use keywords.",
    is_flag=True,
)
@click.pass_obj
def fex_custom_subcommand(obj, force, ngram_max, split_ta, stop_words, use_keywords):
    if not force:
        assert obj.provided.fex is False, dont_reassign_fex_msg
    params = {
        "ngram_max": ngram_max,
        "split_ta": split_ta,
        "stop_words": stop_words,
        "use_keywords": use_keywords,
    }
    obj.config.fex = OneModelConfig(abbr=name, params=params)
    obj.provided.fex = True
