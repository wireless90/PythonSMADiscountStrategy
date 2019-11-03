from datetime import datetime
from binance.client import Client
import pickle


class CandleStickManager:

    
    @staticmethod
    def get_candle_sticks(client, symbol, period='3 months ago UTC', interval=Client.KLINE_INTERVAL_1HOUR):
        klines = client.get_historical_klines(symbol, interval, period)
        return [CandleStick(kline) for kline in klines]   

    @staticmethod
    def save_candle_sticks(candlesticks_list, filepath):
        with open(filepath, 'wb') as file_handler:
            pickle.dump(candlesticks_list, file_handler)


    @staticmethod
    def save_candle_sticks(filepath, client, symbol, period='3 months ago UTC', interval=Client.KLINE_INTERVAL_1HOUR):
        candlesticks_list = CandleStickManager.get_candle_sticks(client, symbol, period, interval)
        with open(filepath, 'wb') as file_handler:
            pickle.dump(candlesticks_list, file_handler)


    @staticmethod
    def get_candle_sticks_from_file(filepath):
        with open(filepath, 'rb') as file_handler:
            return [CandleStick(raw_candlestick) for raw_candlestick in pickle.load(file_handler)]


class CandleStick(object):
    """description of class"""


    def __init__(self, info):
        self.open_time = datetime.fromtimestamp(info[0]/1000).strftime('%Y-%m-%d %H:%M:%S')
        self.open = float(info[1])
        self.high = float(info[2])
        self.low = float(info[3])
        self.close = float(info[4])
        self.volume = float(info[5])
        self.close_time = datetime.fromtimestamp(info[6]/1000).strftime('%Y-%m-%d %H:%M:%S')
        self.quote_asset_volume = float(info[7])
        self.number_of_trades = info[8]
    
    def price_is_below_candle(self, price):
        if self.is_green_candle():
            if price < self.open:
                return True
            else:
                return False
        else:
            if price < self.close:
                return True
            else:
                return False

    def price_is_above_candle(self, price):
        if self.is_green_candle():
            if price > self.close:
                return True
            else:
                return False
        else:
            if price > self.open:
                return True
            else:
                return False

    def price_is_within_open_close(self, price):
        if self.is_green_candle():
            if self.close >= price and self.open <= price:
                return True
            else:
                return False
        else:
            if self.open >= price and self.close <= price:
                return True
            else:
                return False

    
    def is_green_candle(self):
        return self.close > self.open

    def price_is_within_high_low(self, price):
        if high >= price and low <= price:
            return True
        return False

    def __repr__(self):
        return 'Close {}\n'.format(self.open_time)


