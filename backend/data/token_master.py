"""
VTGD Token Master
"""

import requests

MASTER_URL = (
    "https://margincalculator.angelbroking.com/"
    "OpenAPI_File/files/OpenAPIScripMaster.json"
)


def load_master():
    response = requests.get(MASTER_URL, timeout=30)
    response.raise_for_status()
    return response.json()
