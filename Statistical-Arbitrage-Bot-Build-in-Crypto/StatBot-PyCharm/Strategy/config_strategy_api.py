'''
    API Documentation
    https://bybit-exchange.github.io/docs/inverse/#t-introduction

    WebSocket example
    https://github.com/bybit-exchange/pybit/blob/master/examples/websocket_example.py
'''

# API Imports
import pandas as pd
# works only with older version
# pip install pybit==1.3.6
from pybit import HTTP
from pybit import WebSocket

# CONFIG
mode = "test"
# focus is going to be on hourly data (60) and daily ("D")
# available time frames
# https://bybit-exchange.github.io/docs/inverse/#tp-sl-mode-tp_sl_mode
timeframe = 60
# maximum number of history I want to pull when getting historical candlesticks
kline_limit = 200
# z_score works like a moving average
# window of this moving average needs to be configured
# the smaller the number the more aggressive the z-score strategy is going to be
z_score_window = 21
# filename and relative path
data_file = "Data/1_price_list.json"
cointegrated_pairs_file = "Data/2_cointegrated_pairs.csv"
backtest_file = "Data/3_backtest_file.csv"

# LIVE API
api_key_mainnet = ""
api_secret_mainnet = ""

# TEST API
keys_test = pd.read_csv("~/Documents/temp/byb/testnet_key.txt", sep=" ", header=None)
api_key_testnet = keys_test[0][0]
api_secret_testnet = keys_test[0][1]

# SELECTED API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

# API URL
# REST endpoints, documentation at
# https://bybit-exchange.github.io/docs/inverse/#t-authentication
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"

# SESSION Activation
session = HTTP(api_url)

# Web Socket Connection
# https://bybit-exchange.github.io/docs/inverse/#t-websocketauthentication

# subs = [
#     "klineV2.1.BTCUSD"
# ]
# ws = WebSocket(
#     "wss://stream-testnet.bybit.com/realtime",
#     subscriptions = subs
# )
#
# while True:
#     data = ws.fetch(subs[0])
#     if data:
#         print(data)

