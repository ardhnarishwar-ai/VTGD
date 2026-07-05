"""
VTGD Strike Ranking Engine
"""

from .greeks import Greeks
from .net_weight import net_weight
from .diffusion import diffusion_score
from .safety import safety_score


def strike_rank(g: Greeks) -> float:
    """
    VTGD Strike Rank

    Rank =
    (Safety × Diffusion) / Premium

    Higher Positive Rank = Better Strike
    Negative Rank = Trap Strike
    """

    sf = safety_score(g)
    df = diffusion_score(g)

    rank = (sf * df) / (g.premium + 1e-6)

    return round(rank, 4)
