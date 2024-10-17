import json
import requests

url = "https://api.gateio.ws/api/v4/spot/order_book"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
param_btc = {"currency_pair": "BTC_USDT"}
param_eth = {"currency_pair": "ETH_USDT"}
param_sol = {"currency_pair": "SOL_USDT"}
response_btc = requests.get(url=url, params=param_btc, headers=headers)

try:
    if response_btc.status_code == 200:
        json_data = response_btc.json()
        print("Ордербук для BTC:")
        print(f'Ордера на покупку{json_data['bids']}')
        print(f'Ордера на ппродажу{json_data['asks']}')
    elif response_btc.status_code == 400:
        print('Неверный запрос!')
    elif response_btc.status_code == 401:
        print('Требуется аутентификация!')
    elif response_btc.status_code == 403:
        print('Доступ запрещен!')
    elif response_btc.status_code == 404:
        print('Ресурс не найден!')
    elif response_btc.status_code == 429:
        print('Превышен лимит запросов!')
    elif response_btc.status_code == 500:
        print('Внутренняя ошибка сервера!')
    elif response_btc.status_code == 502:
        print('Ошибка шлюза!')
    elif response_btc.status_code == 503:
        print('Сервис недоступен!')
    elif response_btc.status_code == 504:
        print('Таймаут шлюза!')
    else:
        print('Неизвестная ошибка!')
except requests.HTTPError as error:
    print(f'Произошла ошибка: {error}')

response_eth = requests.get(url=url, params=param_eth, headers=headers)

try:
    if response_eth.status_code == 200:
        json_data = response_eth.json()
        print("Ордербук для ETH:")
        print(f'Ордера на покупку{json_data['bids']}')
        print(f'Ордера на ппродажу{json_data['asks']}')
        print(json_data)
    elif response_eth.status_code == 400:
        print('Неверный запрос!')
    elif response_eth.status_code == 401:
        print('Требуется аутентификация!')
    elif response_eth.status_code == 403:
        print('Доступ запрещен!')
    elif response_eth.status_code == 404:
        print('Ресурс не найден!')
    elif response_eth.status_code == 429:
        print('Превышен лимит запросов!')
    elif response_eth.status_code == 500:
        print('Внутренняя ошибка сервера!')
    elif response_eth.status_code == 502:
        print('Ошибка шлюза!')
    elif response_eth.status_code == 503:
        print('Сервис недоступен!')
    elif response_eth.status_code == 504:
        print('Таймаут шлюза!')
    else:
        print('Неизвестная ошибка!')
except requests.HTTPError as error:
    print(f'Произошла ошибка: {error}')

response_sol = requests.get(url=url, params=param_sol, headers=headers)

try:
    if response_sol.status_code == 200:
        json_data = response_sol.json()
        print("Ордербук для SOL:")
        print(f'Ордера на покупку{json_data['bids']}')
        print(f'Ордера на ппродажу{json_data['asks']}')
        print(json_data)
    elif response_sol.status_code == 400:
        print('Неверный запрос!')
    elif response_sol.status_code == 401:
        print('Требуется аутентификация!')
    elif response_sol.status_code == 403:
        print('Доступ запрещен!')
    elif response_sol.status_code == 404:
        print('Ресурс не найден!')
    elif response_sol.status_code == 429:
        print('Превышен лимит запросов!')
    elif response_sol.status_code == 500:
        print('Внутренняя ошибка сервера!')
    elif response_sol.status_code == 502:
        print('Ошибка шлюза!')
    elif response_sol.status_code == 503:
        print('Сервис недоступен!')
    elif response_sol.status_code == 504:
        print('Таймаут шлюза!')
    else:
        print('Неизвестная ошибка!')
except requests.HTTPError as error:
    print(f'Произошла ошибка: {error}')


