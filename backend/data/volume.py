"""
VTGD Relative Volume Engine
"""


def relative_volume(
    current_volume: float,
    average_volume: float,
) -> float:
    """
    Relative Volume (RVOL)

    RVOL =
    Current Volume /
    Average Volume

    RVOL > 1
        Strong Participation

    RVOL < 1
        Weak Participation
    """

    if average_volume <= 0:
        return 0.0

    return round(current_volume / average_volume, 4)
