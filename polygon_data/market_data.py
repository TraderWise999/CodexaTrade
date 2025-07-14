
import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

BASE_URL = "https://api.polygon.io"

def get_current_price(symbol):
    try:
        url = f"{BASE_URL}/v2/last/trade/{symbol.upper()}?apiKey={POLYGON_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['results']['p']
    except Exception as e:
        print(f"Error fetching current price for {symbol}: {e}")
        return None

def get_historical_candles(symbol, timespan="minute", limit=50):
    try:
        url = f"{BASE_URL}/v2/aggs/ticker/{symbol.upper()}/range/1/{timespan}/2023-01-09/2023-01-09?adjusted=true&sort=asc&limit={limit}&apiKey={POLYGON_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['results']
    except Exception as e:
        print(f"Error fetching historical data for {symbol}: {e}")
        return []
