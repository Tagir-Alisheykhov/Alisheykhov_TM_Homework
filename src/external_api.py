import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('KEY_API')

headers = {
    "apikey": API_KEY
}


def currency_conversion(currency: str = 'USD', nominal: int = 1) -> float:
    """ Конвертация входной валюты в рубль """
    response = requests.get((f"https://api.apilayer.com/exchangerates_data/convert?"
                             f"to=RUB&from={currency}&amount={nominal}"), headers=headers)
    status_code = response.status_code
    if status_code == 200:
        conversion_rate = response.json()['result']
        return conversion_rate
    # else:
    #     raise ValueError("Неуспешный код-статус")
