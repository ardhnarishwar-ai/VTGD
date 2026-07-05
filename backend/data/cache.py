"""
VTGD Tick Cache
"""


class TickCache:

    def __init__(self):

        self.previous = {}

    def update(self, symbol, data):

        self.previous[symbol] = data

    def get(self, symbol):

        return self.previous.get(symbol)
