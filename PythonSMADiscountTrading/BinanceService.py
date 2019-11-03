from binance.client import Client

class BinanceService:

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(api_key, api_secret)

    def get_client(self):
        return self.client

    def get_all_symbols(self):
        return self.client.get_all_tickers()


