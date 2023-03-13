import requests
currency = input()
all_exchanges = []
currency_codes = requests.get(f'http://www.floatrates.com/daily/{currency.lower()}.json').json()
while True:
    exchange = input()
    if exchange == '':
        break
    else:
        exchange_rate = currency_codes[exchange.lower()]['rate']
        money = float(input())
        total = round(exchange_rate * money, 2)
        print('Checking the cache...')
        while True:
            if exchange == 'USD' or exchange == 'usd':
                print('Oh! It is in the cache!')
                print(f'You received {total} USD.')
                break
            elif exchange == 'EUR' or exchange == 'eur':
                print('Oh! It is in the cache!')
                print(f'You received {total} EUR.')
                break
            else:
                if str(exchange) in all_exchanges:
                    print('Oh! It is in the cache!')
                    print(f'You received {total} {exchange.upper()}.')
                    all_exchanges.append(exchange)
                    break
                else:
                    print('Sorry, but it is not in the cache!')
                    print(f'You received {total} {exchange.upper()}.')
                    all_exchanges.append(exchange)
                    break
    continue
