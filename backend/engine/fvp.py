"""
VTGD Fair Value Price Engine
"""


def fair_value_price(
    spot: float,
    vwap: float,
) -> dict:
    """
    Fair Value Price

    Returns:
        Price Difference
        Status
    """

    difference = spot - vwap

    if difference > 0:
        status = "ABOVE FVP"

    elif difference < 0:
        status = "BELOW FVP"

    else:
        status = "AT FVP"

    return {
        "difference": round(difference, 2),
        "status": status,
    }
