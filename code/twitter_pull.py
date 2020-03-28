#!/usr/bin/env python3

import sys
import twitter as tw
import TKEYS as KEYS

PYTHONIOENCODING="UTF-8"

def login():
        api = tw.Api(consumer_key = KEYS.CONSUMER_KEY, consumer_secret = KEYS.CONSUMER_SECRET, access_token_key = KEYS.ACCESS_TOKEN_KEY, access_token_secret = KEYS.ACCESS_TOKEN_SECRET, tweet_mode='extended')
        print("\n\nConnected to Twitter\n\n")
        print("Retrieving Tweets...\n")
        results = api.GetUserTimeline(include_rts=False, count=200, exclude_replies=True)
        print(results)

user = sys.argv[1]
user = user.lower()
login()
