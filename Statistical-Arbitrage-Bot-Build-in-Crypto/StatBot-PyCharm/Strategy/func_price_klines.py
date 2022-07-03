"""
    Query Mark Price Kline https://bybit-exchange.github.io/docs/inverse/#t-markpricekline
    interval: 60, "D" # https://bybit-exchange.github.io/docs/inverse/#tp-sl-mode-tp_sl_mode
    from: integer from timestamp in seconds
    limit: max size of 200
"""

from config_strategy_api import session
from config_strategy_api import timeframe
from config_strategy_api import kline_limit
import datetime
import time

# Get start times
time_start_date = 0
if timeframe == 60:
    time_start_date = datetime.datetime.now() - datetime.timedelta(hours=kline_limit)
if timeframe == "D":
    time_start_date = datetime.datetime.now() - datetime.timedelta(days=kline_limit)
time_start_seconds = int(time_start_date.timestamp())

# Get historical prices (klines)
def get_price_klines(symbol):

    # Get prices
    prices = session.query_mark_price_kline(
        symbol = symbol,
        interval = timeframe,
        limit = kline_limit,
        from_time = time_start_seconds
    )

    # Manage API calls
    # To make sure requests are not constantly sent
    time.sleep(0.1)

    # Return output
    # If not enough data is returned (= kline_limit) it's not useful for interpretation
    # In this case empty dictionary gets returned
    if len(prices["result"]) != kline_limit:
        return []
    return prices["result"]