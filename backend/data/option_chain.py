from app.auth.smartapi import login
"""
VTGD Live Option Chain
"""

def get_option_chain(exchange="NFO", symbol="NIFTY"):
    """
    Fetch Option Chain from Angel One
    """

    smart, session = login()

    response = smart.optionGreek(
    {
        "name": symbol,
        "expirydate": "09JUL2026"
    }
)

return response
