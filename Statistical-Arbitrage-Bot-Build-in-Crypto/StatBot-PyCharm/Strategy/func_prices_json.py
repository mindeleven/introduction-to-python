from func_price_klines import get_price_klines
import json
from datetime import datetime

# Store price history for all available pairs
def store_price_history(symbols):

    # Get prices and store in DataFrame
    counts = 0
    price_history_dict = {}
    for sym in symbols:
        symbol_name = sym["name"]
        price_history = get_price_klines(symbol_name)
        if len(price_history) > 0:
            price_history_dict[symbol_name] = price_history
            counts += 1
            print(f"{counts} items stored")
        else:
            print(f"{counts} items not stored")
        # # add counter to make sure api limits as not exceeded
        # counts += 1
        # if counts > 5:
        #     break
        # print(price_history)

    # Output prices to JSON
    if len(price_history_dict) > 0:
        with open(f"Data/1_price_list.json", "w") as fp:
            json.dump(price_history_dict, fp, indent=4)
        print("Prices saved successfully.")

    # Return output
    return
