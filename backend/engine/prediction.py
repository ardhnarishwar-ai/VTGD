"""
VTGD Prediction Engine
"""

from .constants import (
    BUY,
    SELL,
    NEUTRAL,
    DIFFUSION_THRESHOLD,
)


def predict(diffusion: float) -> str:
    """
    Prediction Engine

    Positive Diffusion  -> BUY CALL
    Negative Diffusion  -> BUY PUT
    Near Zero           -> WAIT
    """

    if diffusion > DIFFUSION_THRESHOLD:
        return BUY

    if diffusion < -DIFFUSION_THRESHOLD:
        return SELL

    return NEUTRAL
