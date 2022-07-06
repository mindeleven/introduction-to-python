from statsmodels.tsa.stattools import coint
import statsmodels.api as sm
import pandas as pd
import numpy as np
import math

# Calculate spread
def calculate_spread(series_1, series_2, hedge_ratio):
    spread = pd.DataFrame(series_1) - (pd.Series(series_2) * hedge_ratio)
    return spread

# Calculate co-integration
def calculate_cointegration(series_1, series_2):
    coint_flag = 0
    coint_res = coint(series_1, series_2)
    coint_t = coint_res[0]
    p_value = coint_res[1]
    critical_value = coint_res[2][1] # c value
    # method to find hedge ratio
    model = sm.OLS(series_1, series_2).fit()
    hedge_ratio = model.params[0]
    spread = calculate_spread(series_1, series_2, hedge_ratio)
    # print(spread)
    # how often is zero line crossed ?
    zero_crossings = len(np.where(np.diff(np.sign(spread)))[0])
    # required p-value for cointegration is less than five
    if p_value < 0.5 and coint_t < critical_value:
        coint_flag = 1
    return (
        coint_flag, round(p_value, 2), round(coint_t, 2),
        round(critical_value, 2), round(hedge_ratio, 2), zero_crossings
    )


# Put close prices into a list
def extract_close_prices(prices):
    close_prices = []
    for price_values in prices:
        if math.isnan(price_values["close"]):
            return []
        close_prices.append(price_values["close"])
    # print(close_prices) # print to debug
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
                # make sure that the unique value isn't already in the list
                if unique in included_list:
                    break

                # Get close prices
                series_1 = extract_close_prices(prices[sym_1])
                series_2 = extract_close_prices(prices[sym_2])

                # Check for cointegration and add cointegrated pair
                coint_flag, p_value, t_value, c_value, hedge_ratio, zero_crossings = calculate_cointegration(series_1, series_2)
                # print(coint_flag, p_value) # just to check it works
                # If cointegration found put unique value in List
                if coint_flag == 1:
                    included_list.append(unique)
                    # Saving findings to a spreadsheet like file
                    # to make it easier to analyze it visually
                    coint_pair_list.append({
                        "sym_1": sym_1,
                        "sym_2": sym_2,
                        "p_value": p_value,
                        "t_value": t_value,
                        "c_value": c_value,
                        "hedge_ratio": hedge_ratio,
                        "zero_crossings": zero_crossings
                    })

    # Output results
    df_coint = pd.DataFrame(coint_pair_list)
    # Sort by crossings with zero line with most crossings at the top
    df_coint = df_coint.sort_values("zero_crossings", ascending=False)
    df_coint.to_csv("Data/2_cointegrated_pairs.csv")
    return df_coint