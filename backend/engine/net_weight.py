"""
VTGD Net Weight Engine
"""

from .greeks import Greeks


def net_weight(g: Greeks) -> float:
    """
    VTGD Net Weight

    Buyer Weight =
    (Gamma × |Delta|) × (1 + Volume Ratio)

    Seller Weight =
    (Gamma × |Delta|) × (1 + OI Ratio)

    Net Weight =
    Buyer Weight − Seller Weight
    """

    momentum = g.gamma * abs(g.delta)

    buyer_weight = momentum * (1 + g.volume_ratio)

    seller_weight = momentum * (1 + g.oi_ratio)

    value = buyer_weight - seller_weight

    return round(value, 4)
