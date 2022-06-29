from config_strategy_api import session

# get symbols that are tradable
def get_tradeable_symbols():
    sym_list = []
    symbols = session.query_symbol()
    if "ret_msg" in symbols.keys():
        if symbols["ret_msg"] == "OK":
            symbols = symbols["result"]
    for symbol in symbols:
        # (1) we only want to deal with symbols that are USDT
        # (2) we only want to trade coins that give us a rebate
        # so we're looking for a maker_fee less than zero
        # (3) only coins should be recommended that are tradable
        if symbol["quote_currency"] == "USDT" and float(symbol["maker_fee"]) < 0 and symbol["status"] == "Trading":
            sym_list.append(symbol)

    return sym_list