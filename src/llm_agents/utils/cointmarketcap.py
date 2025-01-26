import requests
from ...config import config

class CoinMarketCapClient:
    def __init__(self):
        self.api_key = config.coinmarketcap.api_key
        self.base_url = config.coinmarketcap.base_url
        self.rate_limit_per_minute = config.coinmarketcap.rate_limit_per_minute
        self.headers = {
            "X-CMC_PRO_API_KEY": self.api_key,
            "Accept": "application/json"
        }


    def get_latest_listings(self, limit: int = 10):
        url = f"{self.base_url}/cryptocurrency/listings/latest"
        params = {
            "limit": limit,
            "start": 1,
            "convert": "USD"
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_price_history(self, symbol: str):
        url = f"{self.base_url}/cryptocurrency/ohlcv/historical"
        params = {
            "symbol": symbol,
            "convert": "USD",
            "time_period": "24h"
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
