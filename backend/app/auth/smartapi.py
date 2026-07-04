from SmartApi import SmartConnect
import pyotp
import os

def create_smartapi():
    api_key = os.getenv("ANGEL_API_KEY")
    return SmartConnect(api_key=api_key)

def login():
    api_key = os.getenv("ANGEL_API_KEY")
    client_id = os.getenv("ANGEL_CLIENT_ID")
    mpin = os.getenv("ANGEL_MPIN")
    totp_secret = os.getenv("ANGEL_TOTP_SECRET")

    smart = SmartConnect(api_key=api_key)

    totp = pyotp.TOTP(totp_secret).now()

    session = smart.generateSession(
        client_id,
        mpin,
        totp
    )

    return smart, session
