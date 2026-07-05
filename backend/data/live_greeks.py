"""
VTGD Live Greeks Parser
"""

from ..engine.greeks import create_greeks


def parse_greeks(option: dict):
    """
    Convert Angel One Option Chain
    into VTGD Greeks object
    """

    return create_greeks(
        delta=float(option.get("delta", 0.0)),
        gamma=float(option.get("gamma", 0.0)),
        theta=float(option.get("theta", 0.0)),
        vega=float(option.get("vega", 0.0)),
        intrinsic=float(option.get("intrinsicValue", 0.0)),
        volume_ratio=0.0,
        oi_ratio=0.0,
        premium=float(option.get("ltp", 0.0)),
    )
