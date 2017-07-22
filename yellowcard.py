#!python3

"""Starts bot on twitter that tweets when internet bandwidth
   goes lower than advertised"""

"""TODO:

"""    

"""DONE:
    -check bandwidth
    -Connect to twitter api using oath
    -post if results meet criteria
    -schedule to run in interval
"""

from twitter import twt
from speedtest import Speedtest
from pprint import pprint


from six import BytesIO
from six.moves.urllib.request import Request, urlopen

import sys
import schedule

DEBUG = True

THRESHOLD = 0.70
ISP_DL = 100
ISP_UP = 100
ISP = "ATT"
MSG = "Hey @{}. What's with {:.0f}Mb/s down?\n" + "I'm paying for {:.0f}Mb/s!\n#speedtest" 

def run_yellowcard():
    """begin running bot. init tweepy connection. post if bandwidth sucks"""

    if(DEBUG):
        print("Starting tweepy bot in debug mode.", flush=True)
        
    st_results = get_speedtest()
    dl = st_results["download"]/1000000
    
    if dl < (ISP_DL*THRESHOLD):
        if(DEBUG):
            print("Current bandwidth is less than advertised: {:.1f}/{:.1f}".format(dl, ISP_DL)) 
        tweet_results(dl)
    else:
        if(DEBUG):
            print("Current bandwidth meets threshold: {:.1f} down / Threshold: {:.1f}. ISP Down: {:.1f}".format(dl, ISP_DL*THRESHOLD,ISP_DL))

def get_speedtest():
    """get current bandwidth using speedtest.net lib"""

    if(DEBUG):
        print("Gathering speedtest results...", flush=True)

    s = Speedtest()
    s.get_best_server()
    s.download()
    
    return s.results.dict()

def tweet_results(dl):
    """Post tweet to account"""

    TWT = twt.get_api()
    try:
        if(DEBUG):
            print("=====Mock Posting=====")
            print(MSG.format(ISP, dl, ISP_DL))
            print("=====End=====", flush=True)
        else:
            TWT.update_status(DEBUG_MSG.format(ISP, dl, ISP_DL))
    except:
        print("error posting to twitter", flush=True)

def repeat_function_mins():
    schedule.schedule_run(run_yellowcard, 5)

if __name__ == '__main__':
    repeat_function_mins()
