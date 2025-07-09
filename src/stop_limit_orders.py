from binance.enums import SIDE_BUY, SIDE_SELL, TIME_IN_FORCE_GTC
from utils import init_client
import logging

def place_stop_limit_order(api_key, api_secret,symbol, side, quantity,price, stop_price):
    client = init_client(api_key, api_secret)

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type="STOP_MARKET",
            stopPrice=str(stop_price),
            limit_price = price,
            quantity=quantity,
            timeInForce=TIME_IN_FORCE_GTC,
        )
        logging.info(f"✅ Stop-limit order placed: {symbol} {side} {quantity} | STOP={stop_price} LIMIT={price}")
        print("✅ Stop-Market order placed successfully!")
        print(order)
    except Exception as e:
        logging.error(f"❌ Failed to place stop-limit order: {e}", exc_info=True)
        print(f"❌ Error placing stop-limit order: {e}")
