"""
VTGD Data Validator
"""

from typing import Dict, Any


REQUIRED_FIELDS = (
    "delta",
    "gamma",
    "theta",
    "vega",
    "ltp",
)


def validate_option(option: Dict[str, Any]) -> bool:
    """
    Validate one option-chain record before
    sending it to the VTGD engine.
    """

    for field in REQUIRED_FIELDS:

        if field not in option:
            return False

        if option[field] is None:
            return False

    if option["ltp"] <= 0:
        return False

    return True
