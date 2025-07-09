from utils import init_logger
import  logging

init_logger()

def place_market_order(symbol, side, quantity, client):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"Market Order: {order}")
        print("✅ Market order placed successfully!")
        print(order)
    except Exception as e:
        logging.error(f"Market Order Error: {e}")
        print(f"❌ Error: {e}")
