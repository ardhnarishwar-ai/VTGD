from SmartApi import SmartConnect
import pyotp
import os

def create_smartapi():
    api_key = os.getenv("ANGEL_API_KEY")
    return SmartConnect(api_key=api_key)
