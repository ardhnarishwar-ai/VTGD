"""
VTGD Diffusion Engine
"""

from math import sqrt

from .greeks import Greeks
from .net_weight import net_weight


def diffusion_score(g: Greeks) -> float:
    """
    VTGD Diffusion

    Diffusion =
    Net Weight × √Vega
    """

    nw = net_weight(g)

    value = nw * sqrt(max(g.vega, 0.0))

    return round(value, 4)
