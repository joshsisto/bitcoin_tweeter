from __future__ import absolute_import, print_function
from datetime import datetime, timedelta
from json import loads
import urllib.request
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

def get_bitcoin_price(endpoint):
    """query the coindesk api"""
    req = urllib.request.Request('http://api.coindesk.com/v1/bpi/{}'.format(endpoint))
    result = urllib.request.urlopen(req)
    resulttext = result.read()
    return loads(resulttext)

def get_current_btc_price():
    """get bitcoin price index in US dollars by querying the coindesk API"""
    return get_bitcoin_price('currentprice.json')['bpi']['USD']


def get_last_years_btc_price():
    """get last years bitcoin price and store is as a variable"""
    global last_year
    last_year = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    endpoint = 'historical/close.json?start={0}&end={0}'.format(last_year)
    return get_bitcoin_price(endpoint)['bpi']


if __name__ == '__main__':

    current_price = get_current_btc_price()
    BTC_USD = ('Current BTC Price: ${rate_float:.2f} USD '.format(**current_price))

    last_years_price = get_last_years_btc_price()
    LY_BTC_USD = ('BTC Price on {}: ${} USD'.format(last_year, last_years_price[last_year]))

    api.update_status(BTC_USD + LY_BTC_USD + ' #bitcoin')  # update status
