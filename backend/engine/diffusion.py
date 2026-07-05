"""
VTGD Diffusion Engine
"""

from .net_weight import net_weight


def diffusion_score(
    buyer_weight: float,
    seller_weight: float,
    diffusion_factor: float = 0.20,
) -> float:
    """
    Market Diffusion

    Diffusion = Net Weight × Diffusion Factor
    """

    nw = net_weight(buyer_weight, seller_weight)

    value = nw * diffusion_factor

    return round(value, 4)
