"""
VTGD Safety Engine
"""

from .physics import (
    chassis,
    engine,
    accelerator,
    fuel,
)


def safety_score(
    delta: float,
    gamma: float,
    vega: float,
    theta: float,
) -> float:
    """
    Vehicle Health

    Safety =
    Chassis
    + (Gamma × Vega)
    - (Theta × Vega)
    """

    value = (
        chassis(delta)
        + (accelerator(gamma) * engine(vega))
        - (fuel(theta) * engine(vega))
    )

    return round(value, 4)
