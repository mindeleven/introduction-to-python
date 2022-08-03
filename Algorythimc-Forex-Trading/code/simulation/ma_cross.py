import pandas as pd
from infrastructure.instrument_collection import instrumentCollection as ic

BUY = 1
SELL = -1
NONE = 0
get_ma_col = lambda x: f"MA_{x}"




def run_ma_sim(
    curr_list=["EUR", "USD"],
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
                    pass # analyse the particular pair