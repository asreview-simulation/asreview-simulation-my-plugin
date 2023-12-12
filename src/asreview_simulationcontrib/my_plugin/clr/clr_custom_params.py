"""
Same as clr-nb from asreview-simulation (but with slightly different defaults),
just for illustration of what a plugin should look like
"""
from typing import Any
from typing import Dict


def clr_custom_params() -> Dict[str, Any]:
    return {
        "alpha": 3.821,
    }
