# 📈 Binance Futures Testnet Trading Bot

This is a command-line Python trading bot that interacts with the Binance Futures Testnet.  
It supports `market`, `limit`, and `stop-limit (STOP_MARKET)` order types with full logging and input validation.

---

## ✅ Features

- ✅ Market, Limit, and Stop-Limit orders
- ✅ Binance Testnet integration (USDT-M Futures)
- ✅ Structured CLI via `argparse`
- ✅ Logs all actions and errors to `bot.log`
- ✅ Modular design (easy to extend)
- ✅ Safe error handling with tracebacks

---

## 🧰 Technologies Used

| Tool            | Purpose                     |
|-----------------|-----------------------------|
| Python 3.10+     | Core language               |
| `python-binance` | Binance API wrapper         |
| `argparse`       | CLI argument parsing        |
| `logging`        | File logging (`bot.log`)    |

---

## 🚀 Quick Start

### 1. Clone & Install


git clone https://github.com/peaceboii/binance-futures-trading-bot.git
cd binance-futures-bot

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
2. 🔑 API Setup
Open src/cli.py and replace:

python
Copy code
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_api_secret"
📌 You can get these keys by enabling Binance Futures Testnet.

📦 Project Structure
arduino
Copy code
project/
├── src/
│   ├── cli.py                  ← Main entry point
│   ├── stop_limit_orders.py    ← STOP_MARKET logic
│   ├── utils.py                ← Client config
│   ├── logger.py               ← Logging setup
├── bot.log                     ← Logs all orders & errors
├── README.md                   ← You are here
└── report.pdf                  ← Final project documentation
📜 Usage
✅ Market Order
(Coming Soon – only stoplimit implemented for this submission)

✅ Stop-Limit Order
bash
Copy code
python src/cli.py stoplimit BTCUSDT BUY 0.01 --price 108400 --stop_price 108500
--stop_price: Price that triggers the market order

--price: Reference limit price (for log clarity)

⚠️ Make sure stop_price follows Binance rules:

For BUY, stop_price > current price

For SELL, stop_price < current price

🪵 Logging
Logs are stored in bot.log with timestamps and error tracebacks:

vbnet
Copy code
2025-07-08 16:30:12,988 - INFO - ✅ Stop-limit order placed: BTCUSDT BUY 0.01 | STOP=108500 LIMIT=108400
2025-07-08 16:31:44,230 - ERROR - ❌ Failed to place order: Order would immediately trigger
Traceback (most recent call last):
  ...
📘 References
Binance Futures Testnet

Binance API Docs

python-binance on PyPI

💡 Future Work
Add .env support for secure key management

Add support for TWAP, Grid, or OCO orders

Optional: GUI using Streamlit

📬 Contact
Built as part of a hiring assignment.
For questions or demo access, contact [kumaravelu].

```bash
