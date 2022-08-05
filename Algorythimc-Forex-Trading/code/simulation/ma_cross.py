import pandas as pd
from infrastructure.instrument_collection import instrumentCollection as ic

class MAResult:
    def __init__(self, df_trades, pairname, ma_l, ma_s):
        self.df_trades = df_trades
        self.pairname = pairname
        self.ma_l = ma_l
        self.ma_s = ma_s,
        self.result = self.result_obj()

    def __repr__(self):
        pass
        # return str(self.result_obj)
    
    def result_obj(self):
        return dict(
            pair = self.pairname,
            num_trades = self.df_trades.shape[0],
            total_gain = int(self.df_trades.GAIN.sum()),
            mean_gain = int(self.df_trades.GAIN.mean()),
            min_gain = int(self.df_trades.GAIN.min()),
            max_gain = int(self.df_trades.GAIN.max()),
            ma_l = self.ma_l,
            ma_s = self.ma_s
        )

BUY = 1
SELL = -1
NONE = 0
get_ma_col = lambda x: f"MA_{x}"

def is_trade(row):
    if row.DELTA >= 0 and row.DELTA_PREV < 0:
        return BUY
    elif row.DELTA < 0 and row.DELTA_PREV >= 0:
        return SELL
    return NONE

def load_price_data(pair, granularity, ma_list):
    # load the data frame for pair and granularity granularity
    df = pd.read_pickle(f"../data/{pair}_{granularity}.pkl")
    # calculate moving averages
    for ma in ma_list:
        df[get_ma_col(ma)] = df.mid_c.rolling(window=ma).mean()
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def get_trades(df_analysis, instrument):
    df_trades = df_analysis[df_analysis.TRADE != NONE].copy()
    df_trades["DIFF"] = df_trades.mid_c.diff().shift(-1)
    df_trades.fillna(0, inplace=True)
    df_trades["GAIN"] = df_trades.DIFF / instrument.pipLocation
    df_trades["GAIN"] = df_trades["GAIN"] * df_trades["TRADE"]
    total_gain = df_trades["GAIN"].sum()
    # return dict(total_gain=int(total_gain), df_trades=df_trades)
    return df_trades

def assess_pair(price_data, ma_l, ma_s, instrument):
    df_analysis = price_data.copy()
    df_analysis["DELTA"] = df_analysis[ma_s] - df_analysis[ma_l]
    df_analysis["DELTA_PREV"] = df_analysis["DELTA"].shift(1)
    df_analysis["TRADE"] = df_analysis.apply(is_trade, axis=1)
    # print(instrument.name, ma_l, ma_s)
    # print(df_analysis.head(3))
    return get_trades(df_analysis, instrument)

def analyse_pair(instrument, granularity, ma_long, ma_short):
    
    ma_list = set(ma_long + ma_short)
    pair = instrument.name

    # load price data
    price_data = load_price_data(pair, granularity, ma_list)
    # print(pair)
    # print(price_data.head(3))

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

            tg = result['total_gain']
            nt = result['df_trades'].shape[0] # rows are first item of shape tuple
         
            print(f"{pair} {granularity} {ma_s}-{ma_l} num-trades: {nt} tot-gain: {tg}")   

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