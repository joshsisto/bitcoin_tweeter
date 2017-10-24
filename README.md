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
Install Tweepy and download the git repo

    pip3 install tweepy
    git clone https://github.com/llamafarmer/bitcoin_tweeter.git
    
Login to dev.twitter.com to create your twitter API keys and tokens. 
[Here](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/) 
is a how-to link.

Update key and token information in tweetBTC.py

Add to cron
