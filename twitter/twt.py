"""Twitter api object creation using oath from config.py.
   Uses Tweepy API wrapper libraryy"""

import tweepy
from twitter import config as c


def get_api():
    """returns tweepy api object"""

    try:
        auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)
        auth.set_access_token(c.access_token, c.access_token_secret)
        api = tweepy.API(auth)
    except tweepy.TweepError as terror:
        print(terror)

    return api