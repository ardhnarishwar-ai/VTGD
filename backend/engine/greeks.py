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

    intrinsic: float
    volume_ratio: float
    oi_ratio: float
    premium: float

def create_greeks(
    delta: float,
    gamma: float,
    theta: float,
    vega: float,
    intrinsic: float,
    volume_ratio: float,
    oi_ratio: float,
    premium: float,
) -> Greeks:

    return Greeks(
        delta=delta,
        gamma=gamma,
        theta=theta,
        vega=vega,
        intrinsic=intrinsic,
        volume_ratio=volume_ratio,
        oi_ratio=oi_ratio,
        premium=premium,
    )


def normalized_delta(delta: float) -> float:
    return abs(delta)


def normalized_gamma(gamma: float) -> float:
    return max(0.0, gamma)


def normalized_theta(theta: float) -> float:
    return abs(theta)


def normalized_vega(vega: float) -> float:
    return max(0.0, vega)
