
import argparse
from utils import init_client
from market_orders import place_market_order
from limit_orders import place_limit_order
from stop_limit_orders import place_stop_limit_order
from logger import init_logger
from utils import load_keys
import logging
import os
from dotenv import load_dotenv

load_dotenv()
init_logger()


API_KEY = os.getenv("API_KEY")
API_SECRET =os.getenv("API_SECRET")

client = init_client(API_KEY, API_SECRET)

parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

parser.add_argument("type", choices=["market", "limit","stoplimit"], help="Order type")
parser.add_argument("symbol", help="Symbol (e.g., BTCUSDT)")
parser.add_argument("side", choices=["BUY", "SELL"], help="BUY or SELL")
parser.add_argument("quantity", type=float, help="Quantity")
parser.add_argument("--price", type=float, help="Required for LIMIT order")
parser.add_argument("--stop_price", type=float, help="Stop trigger price (required for stop-limit orders)")


args = parser.parse_args()

if args.type == "market":
    place_market_order(args.symbol, args.side, args.quantity, client)
elif args.type == "limit":
    if not args.price:
        print("❗ Price is required for limit order.")
    else:
        place_limit_order(args.symbol, args.side, args.quantity, args.price, client)
elif args.type == "stoplimit":
    if not args.price or not args.stop_price:
        print("❌ Both limit and stop price are required for stop-limit order")
    else:
        place_stop_limit_order(
            API_KEY,
            API_SECRET,
            args.symbol,
            args.side,
            args.quantity,
            args.price,
            args.stop_price,

        )



