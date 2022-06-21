import json
import requests
response = requests.get("https://api.exchange.coinbase.com/currencies")


def d_print(obj):
    text = json.dumps(obj, indent=2, sort_keys=True)
    print(text)


def dict_print(dict):
    keys = list(dict.keys())
    for i in range(len(keys)):
        print(f'{keys[i]} : {dict.get(keys[i])}')


def print_all_currencies():
    length = len(response.json())
    currencies = {}
    for i in range(length):
        coin_id = response.json()[i].get('id')
        coin_name = response.json()[i].get('name')
        coin_network = response.json()[i].get('default_network')
        currencies[coin_id] = [coin_name, coin_network]
    dict_print(currencies)


#print(response.json())
print_all_currencies()
