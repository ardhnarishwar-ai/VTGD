from engine.greeks import Greeks
from engine.net_weight import net_weight
from engine.diffusion import diffusion_score
from engine.safety import safety_score
from engine.strike_ranking import strike_rank
"""
VTGD Master Engine
"""
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
