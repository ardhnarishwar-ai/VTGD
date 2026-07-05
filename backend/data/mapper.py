"""
VTGD Data Mapper
"""

from ..engine.greeks import create_greeks


def map_option(option):

    return create_greeks(

        delta=float(option["delta"]),

        gamma=float(option["gamma"]),

        theta=float(option["theta"]),

        vega=float(option["vega"]),

        intrinsic=float(option.get("intrinsicValue",0)),

        volume_ratio=0.0,

        oi_ratio=0.0,

        premium=float(option["ltp"])

    )
