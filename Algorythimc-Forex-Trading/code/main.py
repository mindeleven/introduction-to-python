from api.oanda_api import OandaApi

from infrastructure.instrument_collection import instrumentCollection

if __name__ == '__main__':
   api = OandaApi()

   #data = api.get_account_summary()
   #print(data)

   instrumentCollection.LoadInstruments("../data")
   instrumentCollection.PrintInstruments()