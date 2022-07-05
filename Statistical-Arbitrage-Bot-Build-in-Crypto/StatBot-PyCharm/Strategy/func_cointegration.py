from statsmodels.tsa.stattools import coint
import math

# Calculate co-integration
def calculate_cointegration(series_1, series_2):
    coint_flag = 0
    coint_res = coint(series_1, series_2)
    coint_t = coint_res[0]
    p_value = coint_res[1]
    critical_value = coint_res[2][1] # c value


# Put close prices into a list
def extract_close_prices(prices):
    close_prices = []
    for price_values in prices:
        if math.isnan(price_values["close"]):
            return []
        close_prices.append(price_values["close"])
    print(close_prices)
    return close_prices

# Calculate cointegrated pairs
def get_cointegrated_pairs(prices):
    # Loop through all the coins and check for co-integration
    coint_pair_list = []
    included_list = []
    for sym_1 in prices.keys():
        # print(sym_1)
        # Check each coin against the first (sym_1)
        for sym_2 in prices.keys():
            # We're looping through all the coins once again
            # But only want the once we don't already have (which is only sym_1)
            if sym_2 != sym_1:
                # print(sym_1, sym_2)
                # Get unique combination id and ensure one off check
                sorted_characters = sorted(sym_1 + sym_2)
                unique = "".join(sorted_characters)
                if unique in included_list:
                    break

                # Get close prices
                series_1 = extract_close_prices(prices[sym_1])
                series_2 = extract_close_prices(prices[sym_2])
