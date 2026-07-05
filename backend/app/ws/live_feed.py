"""
VTGD Live Feed
"""

from app.auth.smartapi import login
from data.cache import TickCache

cache = TickCache()


def start_live_feed():
    """
    Starts Angel One live market feed.
    (WebSocket integration will be added next)
    """

    smart, session = login()

    print("✅ Angel One Connected")
    print("🚀 VTGD Live Feed Started")

    return smart
