from ..engine.greeks import create_greeks
from .volume import relative_volume
from .open_interest import oi_ratio
"""
VTGD Data Mapper
"""
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
