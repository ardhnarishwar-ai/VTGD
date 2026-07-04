from SmartApi import SmartConnect
import pyotp
import os

def create_smartapi():
    api_key = os.getenv("tzP4cDZy")
    return SmartConnect(api_key=api_key)

def login():
    api_key = os.getenv("tzP4cDZy")
    client_id = os.getenv("AAAQ844597")
    mpin = os.getenv("2007")
    totp_secret = os.getenv("CS45NEJL52JREY5Y3TIDXLCNDU")

    smart = SmartConnect(api_key=api_key)

    totp = pyotp.TOTP(totp_secret).now()

    session = smart.generateSession(
        client_id,
        mpin,
        totp
    )

    return smart, session
