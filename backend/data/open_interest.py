"""
VTGD Open Interest Engine
"""


def oi_ratio(
    current_oi: float,
    previous_oi: float,
) -> float:
    """
    OI Ratio

    OI Ratio =
    (Current OI - Previous OI)
    / Previous OI

    Positive  -> Seller Build-up

    Negative  -> Short Covering
    """

    if previous_oi <= 0:
        return 0.0

    ratio = (
        current_oi - previous_oi
    ) / previous_oi

    return round(ratio, 4)
