import requests

MASTER_URL = (
    "https://margincalculator.angelbroking.com/"
    "OpenAPI_File/files/OpenAPIScripMaster.json"
)

def load_master():
    response = requests.get(MASTER_URL, timeout=30)
    response.raise_for_status()
    return response.json()

MASTER = load_master()


def search(symbol):
    return [
        s for s in MASTER
        if symbol.upper() in s["symbol"].upper()
    ]


def get_token(symbol):
    result = search(symbol)

    if not result:
        return None

    return result[0]["token"]
