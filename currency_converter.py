import requests
currency = input()
all_exchanges = []
currency_codes = requests.get(f'http://www.floatrates.com/daily/{currency.lower()}.json').json()

cache = {}

if 'usd' in currency_codes:
    cache['usd'] = currency_codes['usd']['rate']
if 'eur' in currency_codes:
    cache['eur'] = currency_codes['eur']['rate']


if __name__ == '__main__':
    while True:
        exchange = input().lower()
        if exchange == '':
            break
        else:
            money = float(input())

            print('Checking the cache...')
            if exchange in cache:
                print('Oh! It is in the cache!')
                exchange_rate = cache[exchange]
            else:
                print('Sorry, but it is not in the cache!')
                exchange_rate = currency_codes[exchange]['rate']
                cache[exchange] = exchange_rate

            total = round(exchange_rate * money, 2)
            print(f'You received {total} {exchange.upper()}.')
