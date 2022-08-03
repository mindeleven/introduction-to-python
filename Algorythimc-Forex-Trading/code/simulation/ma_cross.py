import pandas as pd
from infrastructure.instrument_collection import instrumentCollection as ic

BUY = 1
SELL = -1
NONE = 0
get_ma_col = lambda x: f"MA_{x}"


def load_price_data(pair, granularity, ma_list):
    # load the data frame for pair and granularity granularity
    df = pd.read_pickle(f"../data/{pair}_{granularity}.pkl")
    # calculate moving averages
    for ma in ma_list:
        df[get_ma_col(ma)] = df.mid_c.rolling(window=ma).mean()
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def is_trade():
    pass

def assess_pair(price_data, ma_l, ma_s, instrument):
    df_analysis = price_data.copy()
    df_analysis["DELTA"] = df_analysis[ma_s] - df_analysis[ma_l]
    df_analysis["DELTA_PREV"] = df_analysis["DELTA"].shift(1)
    df_analysis["TRADE"] = df_analysis.apply(is_trade, axis=1)
    return None

def analyse_pair(instrument, granularity, ma_long, ma_short):
    
    ma_list = set(ma_long + ma_short)
    pair = instrument.name

    # load price data
    price_data = load_price_data(pair, granularity, ma_list)
    print(pair)
    print(price_data.head(3))

    # assess a pair
    for ma_l in ma_long:
        for ma_s in ma_short:
            if ma_l <= ma_s:
                continue

            result = assess_pair(
                price_data,
                get_ma_col(ma_l),
                get_ma_col(ma_s),
                instrument
            )



def run_ma_sim(
    curr_list=["EUR", "USD", "AUD", "GBP"],
    granularity=["H1"],
    ma_long=[20, 40, 80],
    ma_short=[10, 20]
):
    ic.LoadInstruments("../data")
    for g in granularity:
        for p1 in curr_list:
            for p2 in curr_list:
                pair = f"{p1}_{p2}"
                # check if pait in currency list
                if pair in ic.instruments_dict.keys():
                    analyse_pair(ic.instruments_dict[pair], g, ma_long, ma_short)