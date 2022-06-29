from func_price_klines import get_price_klines
import json

# Store price history for all available pairs
def store_price_history(symbols):

    # Get prices and store in DataFrame
    counts = 0
    price_history_dict = {}
    for sym in symbols:
        symbol_name = sym["name"]
        price_history = get_price_klines(symbol_name)

    print(price_history)