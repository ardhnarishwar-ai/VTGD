"""
VTGD Net Weight Engine
"""


def net_weight(
    buyer_weight: float,
    seller_weight: float,
) -> float:
    """
    Net Weight =
    Buyer Weight - Seller Weight
    """

    value = buyer_weight - seller_weight

    return round(value, 4)
