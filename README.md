# bitcoin_tweeter
Python 3.4.2 | tweepy 3.5.0

This 
[twitter bot](https://twitter.com/Evil_1T) 
uses the 
[coindesk API](https://www.coindesk.com/api/) 
to tweet the current bitcoin price and the price of bitcoin last year.

The code is written in Python 3 and uses the 
[Tweepy](http://www.tweepy.org/) 
python library to send tweets. 

## Installation and Setup
### 1. Set Up Auth
The authentication keys for the different APIs are read from shell environment
variables. Each service has different steps to obtain them.

#### Twitter

Log in to your [Twitter](https://twitter.com/) account and
[create a new application](https://apps.twitter.com/app/new). Under the *Keys
and Access Tokens* tab for [your app](https://apps.twitter.com/) you'll find
the *Consumer Key* and *Consumer Secret*. Update [`credentials`](credentials.py) with your 
*Consumer Key* and *Consumer Secret*

If you want the tweets to come from the same account that owns the application,
simply use the *Access Token* and *Access Token Secret* on the same page. If
you want to tweet from a different account, follow the
[steps to obtain an access token](https://dev.twitter.com/oauth/overview). Then
update [`credentials`](credentials.py) with your *Access Token* and *Access Token Secret*

### 2. Install Dependencies

Currently there is one dependency you need to install
[pip](https://pip.pypa.io/en/stable/quickstart/):

```shell
$ pip install -r requirements.txt
```

### 3. Test

### 4. Add to Cron
