from fileinput import filename


import json
from models.instrument import Instrument 

class InstrumentCollection:
    FILENAME = "instruments.json"
    API_KEYS = ['name', 'type', 'displayName', 'pipLocation', 'displayPrecision', 
         'tradeUnitsPrecision', 'marginRate']

    def __init__(self):
        self.instruments_dict = {}

    def LoadInstruments(self, path):
        self.instruments_dict = {}
        fileName = f"{path}/{self.FILENAME}"
        with open(fileName, "r") as f:
            data = json.loads(f.read())
            for k, v in data.items():
                # create instrument class for each instrument
                self.instruments_dict[k] = Instrument.FromApiObject(v)
    
    def PrintInstruments(self):
        [print(k,v) for k,v in self.instruments_dict.items()]
        print(len(self.instruments_dict.keys()), "instruments")

# instantiate class whenever model gets imported
instrumentCollection = InstrumentCollection()

