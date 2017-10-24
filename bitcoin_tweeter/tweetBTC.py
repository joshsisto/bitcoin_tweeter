from __future__ import absolute_import, print_function
from datetime import datetime, timedelta
from json import loads
from urllib import urlopen

import tweepy
import time

# Import credentials from credentials.py
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

#Bitcoin

def get_bitcoin_price(endpoint):
    req = urlopen('http://api.coindesk.com/v1/bpi/{}'.format(endpoint))
    return loads(req.read())


def get_current_btc_price():
    return get_bitcoin_price('currentprice.json')['bpi']['USD']


def get_last_years_btc_price():
    last_year = (datetime.now() - timedelta(days=366)).strftime('%Y-%m-%d')
    endpoint = 'historical/close.json?start={0}&end={0}'.format(last_year)
    return get_bitcoin_price(endpoint)['bpi']


if __name__ == '__main__':

    while True:

        current_price = get_current_btc_price()
        pri = ('Current BTC Price: ${rate_float:.2f} USD '.format(**current_price))

        last_years_price = get_last_years_btc_price()
        pri2 = ('BTC Price on {}: ${:.2f} USD'.format(*last_years_price.items()[0]))

        api.update_status(pri + pri2 + ' #bitcoin')     # update status
        time.sleep(86400)                               # wait 24 hours

# End of Bitcoin
