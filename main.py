#!python3

"""Starts bot on twitter that tweets when internet bandwidth
   goes lower than advertised"""

"""TODO:
    -create new twitter acct
    -Connect to twitter api using oath
    -setup cli params for configuring polling rate, bandwidth-limit and company
    -check bandwidth
    -post if results meet criteria"""

from twitter import twt
from speedtest import Speedtest
from pprint import pprint

from six import BytesIO
from six.moves.urllib.request import Request, urlopen

THRESHOLD = 0.70
ISP_DL = 100
ISP_UP = 100
ISP = "ATT"
MSG = "Hey @{}. What's with {:.0f}Mb/s down?\n" + "I'm paying for {:.0f}Mb/s!\n#speedtest" 

POST_IMG = False

def run():
    """begin running bot. init tweepy connection. post if bandwidth sucks"""
    print("Starting tweepy bot...")
    
    results = get_st()
    dl = results["download"]/1000000
    
    if dl < (ISP_DL*THRESHOLD):
        print("Current bandwidth is less than advertised: {:.1f}/{:.1f}".format(dl, ISP_DL)) 
        tweet_results(dl)
    else:
        print("Current bandwidth meets threshold: {:.1f} down / Threshold: {:.1f}. ISP Down: {:.1f}".format(dl, ISP_DL*THRESHOLD,ISP_DL))

def get_st():
    """get current bandwidth using speedtest.net lib"""
    print("Starting speedtest...")

    s = Speedtest()
    s.get_best_server()
    s.download()
    
    return s.results.dict()

def tweet_results(dl):
    """Post tweet to account"""
    print("=====Posting to Twitter=====")
    print(MSG.format(ISP, dl, ISP_DL))
    print("=====End=====")

    TWT = twt.get_api()
    try:
        TWT.update_status(MSG.format(ISP, dl, ISP_DL))
    except:
        print("error posting to twitter")

if __name__ == '__main__':
    run()
1