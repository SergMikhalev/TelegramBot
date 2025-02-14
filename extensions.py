import json
from multiprocessing.sharedctypes import Value

import requests
from config import keys
import telebot

class ConvertionExeption(Exception):
    pass

class CryproConverter:
    @staticmethod
    def convert(quot:str,base:str,amount:str):


        if quot == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quot_ticker = keys[quot]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту{quot}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обоаботать количество {amount}')
        #r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={quot_ticker},{base_ticker}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={quot_ticker},,{base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base




