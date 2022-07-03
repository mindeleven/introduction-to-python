
# Calculate cointegrated pairs
def get_cointegrated_pairs(prices):
    # Loop through all the coins and check for co-integration
    code_pair_list = []
    included_list = []
    for sym_1 in prices.keys():
        print(sym_1)