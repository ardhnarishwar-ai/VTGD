"""
VTGD Greeks Engine
"""

from dataclasses import dataclass


@dataclass
class Greeks:
    delta: float
    gamma: float
    theta: float
    vega: float


def create_greeks(
    delta: float,
    gamma: float,
    theta: float,
    vega: float,
) -> Greeks:
    """
    Create Greeks object
    """

    return Greeks(
        delta=delta,
        gamma=gamma,
        theta=theta,
        vega=vega,
    )


def normalized_delta(delta: float) -> float:
    return abs(delta)


def normalized_gamma(gamma: float) -> float:
    return max(0.0, gamma)


def normalized_theta(theta: float) -> float:
    return abs(theta)


def normalized_vega(vega: float) -> float:
    return max(0.0, vega)
