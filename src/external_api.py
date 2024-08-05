import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('KEY_API')

headers = {
    "apikey": API_KEY
}


def currency_conversion(currency: str = 'USD', nominal: int = 1) -> list[dict]:
    """ Конвертация входной валюты в рубль """
    response = requests.get((f"https://api.apilayer.com/exchangerates_data/convert?"
                             f"to=RUB&from={currency}&amount={nominal}"), headers=headers)
    if response.status_code == 200:
        return response.json()['result']
    else:
        raise ValueError(f"Не успешный запрос: {response.status_code}")





#        видно выходит список, но почему нет итерации?

#        можно найти индекс по примеру для того чтобы обработать ошибку:
#               return repo['result']
#            ~~~~^^^^^^^^^^
# TypeError: string indices must be integers, not 'str'
#
#
#


# success
# query
# info
# date
# result
# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 1}, 'info': {'timestamp': 1722953164, 'rate': 85.547234}, 'date': '2024-08-06', 'result': 85.547234}
