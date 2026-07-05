from SmartApi.smartWebSocketV2 import SmartWebSocketV2
"""
VTGD Live Feed
"""

from app.auth.smartapi import login
from data.cache import TickCache

cache = TickCache()


def start_live_feed():
    smart, session = login()
    """
    Starts Angel One live market feed.
    (WebSocket integration will be added next)
    """
feed_token = smart.getfeedToken()

sws = SmartWebSocketV2(
    session.authToken,
    "YOUR_API_KEY",
    session.clientCode,
    feed_token
)

def on_data(wsapp, message):
    print(message)

def on_open(wsapp):
    print("🟢 WebSocket Connected")

def on_error(wsapp, error):
    print(error)

def on_close(wsapp):
    print("🔴 WebSocket Closed")

sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

return sws
