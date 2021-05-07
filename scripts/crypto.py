#!/usr/bin/env python3

from binance.client import Client
import configparser
import sys
import requests
from decimal import Decimal

config = configparser.ConfigParser()

# File must be opened with utf-8 explicitly
with open('/home/matteo/.config/polybar/modules/crypto_config', 'r', encoding='utf-8') as f:
	config.read_file(f)

# Everything except the general section
currencies = [x for x in config.sections() if x != 'general']
base_currency = config['general']['base_currency']
params = {'convert': base_currency}

client = Client()
tickers = client.get_all_tickers()
tickers = {d['symbol']:d['price'] for d in tickers}

for currency in currencies:
    icon = config[currency]['icon']
    tick = config[currency]['ticker']
    local_price = float(tickers[tick+base_currency])
    if local_price>100:
        local_price = int(local_price)
    else:
        local_price = round(local_price,1)
    #change_24 = float(json['percent_change_24h'])

    display_opt = config['general']['display']
    if display_opt == 'both' or display_opt == None:
        sys.stdout.write(f'{icon} {local_price}/{change_24:+}%  ')
    elif display_opt == 'percentage':
        sys.stdout.write(f'{icon} {change_24:+}%  ')
    elif display_opt == 'price':
        sys.stdout.write(f'{icon} {local_price}  ')
