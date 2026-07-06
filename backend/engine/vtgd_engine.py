"""
VTGD Master Engine
"""

from greeks import Greeks
from net_weight import net_weight
from diffusion import diffusion_score
from safety import safety_score
from strike_ranking import strike_rank


def evaluate(g: Greeks) -> dict:
    """
    Complete VTGD Evaluation
    """

    nw = net_weight(g)
    df = diffusion_score(g)
    sf = safety_score(g)
    rank = strike_rank(g)

    return {
        "buyer_weight":
            round((g.gamma * abs(g.delta)) * (1 + g.volume_ratio), 4),

        "seller_weight":
            round((g.gamma * abs(g.delta)) * (1 + g.oi_ratio), 4),

        "net_weight": nw,

        "diffusion": df,

        "safety": sf,

        "strike_rank": rank,
    }
