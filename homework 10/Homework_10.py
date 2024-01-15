import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self, url):
        self.url = url
        self.rates = {}

    def parse_exchange_rates(self):
        response = requests.get(self.url)
        soup = BeautifulSoup, (' usd_rate = soup.select_one')

    def convert_to_usd(self, amount, currency_code):
        if currency_code in self.rates:
            converted_amount = amount / self.rates[currency_code]
            return converted_amount
        else:
            return None

converter = CurrencyConverter(url='https://privatbank.ua/rates-archive')
converter.parse_exchange_rates()

amount = float(input('Введіть суму валюти вашої країни: '))
currency_code = input('Введіть код валюти вашої країни (наприклад, USD, EUR, etc.): ')

result = converter.convert_to_usd(amount, currency_code)
if result is not None:
    print(f'Ваша сума у доларах США: {result:.2f}')
else:
    print('Немає інформації про курс для введеної валюти.')