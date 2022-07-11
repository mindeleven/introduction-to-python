from func_cointegration import extract_close_prices
from func_cointegration import calculate_cointegration
from func_cointegration import calculate_spread
from func_cointegration import extract_close_prices
from func_cointegration import calculate_zscore
import matplotlib.pyplot as plt
import pandas as pd


# Plot prices and trends
def plot_trends(sym_1, sym_2, price_data):

    # Extract prices
    prices_1 = extract_close_prices(price_data[sym_1])
    prices_2 = extract_close_prices(price_data[sym_2])

    # Get spread and zscore
    coint_flag, p_value, t_value, c_value, hedge_ratio, zero_crossings = calculate_cointegration(prices_1, prices_2)
    spread = calculate_spread(prices_1, prices_2, hedge_ratio)
    zscore = calculate_zscore(spread)

    print(zscore)