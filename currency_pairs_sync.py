import json
import requests
import time

date = '2022-06-20'
pairs = ['X:ETHUSD', 'X:ETHBTC', 'X:BTCUSD', 'X:ETHUSD', 'X:ETHBTC', 'X:BTCUSD', 'X:ETHUSD', 'X:ETHBTC', 'X:BTCUSD']
responses = []
start = time.time()
for pair in pairs:
    response = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{pair}/range/1/day/{date}/{date}?adjusted"
                        "=true&sort=asc&limit=120&apiKey=E0sAie4Hp3A7hgoYL4rzFfMFuk4SqkMp")
    responses.append(response)
    print('Response obtained successfully')
end = time.time()
total = end - start
print(total)

def process(responded_list):
    for res in responded_list:
        info = res.json()
        if 'ticker' in info.keys():
            print('_'*5, info['ticker'], '_'*5)
            print('Highest = ', info['results'][0]['h'])
            print('Average = ', info['results'][0]['c'])
            print('Lowest = ', info['results'][0]['l'])
            print('_'*20)
        else:
            print(info['error'])


process(responses)
