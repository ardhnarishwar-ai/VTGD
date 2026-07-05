"""
VTGD Safety Engine
"""

from .greeks import Greeks


def safety_score(g: Greeks) -> float:
    """
    VTGD Safety

    Safety =
    (Intrinsic × |Delta|)
    + (Gamma × Vega)
    - (|Theta| × Vega)
    """

    value = (
        (g.intrinsic * abs(g.delta))
        + (g.gamma * g.vega)
        - (abs(g.theta) * g.vega)
    )

    return round(value, 4)
