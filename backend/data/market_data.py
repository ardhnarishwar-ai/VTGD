"""
VTGD Market Data Engine
"""

from ..app.auth.smartapi import login


def get_market_data(exchange="NSE", symbol="NIFTY"):
    """
    Fetch Live Market Data
    """

    smart, session = login()

    response = smart.ltpData(
        exchange=exchange,
        tradingsymbol=symbol,
        symboltoken=""
    )

    return response
