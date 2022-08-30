import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(quote:str, base:str, amount:str):

        if quote == base:
            raise ConvertionExeption(f'Не удалось конвертировать одинаковые валюты: {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту: {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество: {amount}')

        url = f"https://api.apilayer.com/fixer/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"
        payload = {}
        headers = {"apikey": "9eKzf05pNtGrsJ6cHbm8hF5DskU2fHH3"}

        response = requests.request("GET", url, headers=headers, data=payload)
        total_base = round(json.loads(response.content)['result'], 4)
        return total_base
