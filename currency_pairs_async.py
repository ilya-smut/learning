import asyncio
import aiohttp
import time


class RateChecker:
    date = '2022-06-20'
    pairs = ['X:ETHUSD', 'X:ETHBTC', 'X:BTCUSD', 'X:ETHUSD', 'X:ETHBTC', 'X:BTCUSD', 'X:ETHUSD', 'X:ETHBTC', 'X:BTCUSD']
    results = []

    def get_tasks(self, session):
        tasks = []
        for pair in self.pairs:
            tasks.append(asyncio.create_task(session.get(f"https://api.polygon.io/v2/aggs/ticker/{pair}/range/1/day/{self.date}/{self.date}?adjusted=true&sort=asc&limit=120&apiKey=E0sAie4Hp3A7hgoYL4rzFfMFuk4SqkMp", ssl=False)))
        return tasks

    async def get_rates(self):
        async with aiohttp.ClientSession() as session:
            tasks = self.get_tasks(session)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                self.results.append(await response.json())

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.get_rates())

    def process(self):
        self.run()
        for info in self.results:
            #print(info)
            if 'ticker' in info.keys():
                print('_' * 5, info['ticker'], '_' * 5)
                print('Highest = ', info['results'][0]['h'])
                print('Average = ', info['results'][0]['c'])
                print('Lowest = ', info['results'][0]['l'])
                print('_' * 20)
            else:
                print(info['error'])


rate_checker = RateChecker()
rate_checker.process()
