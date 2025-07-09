# src/limit_orders.py
from utils import init_logger
import  logging

init_logger()

def place_limit_order(symbol, side, quantity, price, client):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        logging.info(f"✅ limit order placed: {symbol} {side} {quantity} |  LIMIT={price}")
        print("✅ Limit order placed successfully!")
        print(order)
    except Exception as e:
        logging.error(f"❌ Failed to place limit order: {e}", exc_info=True)
        print(f"❌ Error: {e}")
