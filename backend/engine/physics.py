"""
VTGD Vehicle Physics
"""

from .constants import *


def chassis(delta: float) -> float:
    """
    Chassis = |Delta|
    """
    return abs(delta)


def engine(vega: float) -> float:
    """
    Engine = Vega
    """
    return vega


def accelerator(gamma: float) -> float:
    """
    Accelerator = Gamma
    """
    return gamma


def fuel(theta: float) -> float:
    """
    Fuel = Theta
    """
    return theta
