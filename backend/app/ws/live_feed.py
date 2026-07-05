from config.settings import API_KEY
from data.token_master import get_token
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
symbol = "NIFTY"
token = get_token(symbol)
sws = SmartWebSocketV2(
    session.authToken,
    API_KEY,
    session.clientCode,
    feed_token
)

def on_data(wsapp, message):
    try:
        print(
            f"📈 {symbol} | "
            f"LTP: {message.get('last_traded_price')} | "
            f"Token: {message.get('token')}"
        )
    except Exception:
        print(message)

def on_open(wsapp):

    print("🟢 WebSocket Connected")

    sws.subscribe(
        correlation_id="vtgd",
        mode=1,
        token_list=[
            {
                "exchangeType": 1,
                "tokens": [token]
            }
        ]
    )

    print(f"📡 {symbol} Subscribed")

def on_error(wsapp, error):
    print(error)

def on_close(wsapp):
    print("🔴 WebSocket Closed")

sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close
print("🚀 Starting Angel One WebSocket...")
sws.connect()
return sws
