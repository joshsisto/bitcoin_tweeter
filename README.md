# bitcoin_tweeter
Python 3.4.2 | tweepy 3.5.0

<img src="/images/pythonlogo.png" alt="Python Logo" style="width: 200px;"/> <img src="/images/twittercoin.jpg" alt="Twitter and Bitcoin" style="width: 200px;"/> <img src="/images/Raspberry-Pi-Zero-FL.jpg" alt="Pi Zero" style="width: 200px;"/>

This 
[twitter bot](https://twitter.com/Evil_1T) 
uses the 
[coindesk API](https://www.coindesk.com/api/) 
to tweet the current bitcoin price and the price of bitcoin last year.

The code is written in Python 3 and uses the 
[Tweepy](http://www.tweepy.org/) 
python library to send tweets. Currently running on my 
[raspberry pi](http://amzn.to/2zCPAxu).

## Installation and Setup
### 1. Set Up Auth
The authentication keys for the different APIs are stored in the [`credentials module`](/bitcoin_tweeter/credentials.py)

#### Twitter

Log in to your [Twitter](https://twitter.com/) account and
[create a new application](https://apps.twitter.com/app/new). Under the *Keys
and Access Tokens* tab for [your app](https://apps.twitter.com/) you'll find
the *Consumer Key* and *Consumer Secret*. Update [`credentials`](/bitcoin_tweeter/credentials.py) with your 
*Consumer Key* and *Consumer Secret*

If you want the tweets to come from the same account that owns the application,
simply use the *Access Token* and *Access Token Secret* on the same page. If
you want to tweet from a different account, follow the
[steps to obtain an access token](https://dev.twitter.com/oauth/overview). Then
update [`credentials`](/bitcoin_tweeter/credentials.py) with your *Access Token* and *Access Token Secret*

### 2. Install Dependencies

Currently there is one dependency you need to install
[pip](https://pip.pypa.io/en/stable/quickstart/):

```shell
$ pip3 install -r requirements.txt
```

### 3. Add to Cron
Add script to cron

```shell
$ sudo crontab -e
```

Add the line below to cron and then press ctrl+x to exit and y to save

```shell
0 8,20 * * * python3 <location to your script>/tweetBTC.py
```

The line above will execute the script at 8AM and 8PM everyday

Note: Make sure to update ```<location to your script>``` with the path to your script.

For example: /home/pi/bitcoin_tweeter
