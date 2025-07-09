import logging
import os
from binance.client import Client
from dotenv import load_dotenv
from binance.enums import *

def load_keys():
    load_dotenv()
    return os.getenv("API_KEY"),os.getenv("API_SECRET")

def init_logger():
    logging.basicConfig(
        filename="bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def init_client(api_key, api_secret):
    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    return client
