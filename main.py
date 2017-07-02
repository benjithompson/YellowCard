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
import speedtest
from pprint import pprint
import time

WAIT = 300 #in seconds

def run():
    """begin running bot. init tweepy connection. post if bandwidth sucks"""
    print("Starting bot...")


    #create tweepy using oath
    TWT = twt.get_api()
    if TWT is not None:

        #poll bandwidth and tweet if lower than advertised speed (100Mb/s)
        while(True):
            st = get_st()
            dlspeed = st["download"]
            dlspeed = '{:.2f}'.format(dlspeed/1000000) + "Mb/s"
            print(dlspeed)

            #wait 5 mins
            print('Wait: ' + str(WAIT) + ' secs')
            time.sleep(300) 

def get_st():
    """get current bandwidth using speedtest.net lib"""
    print("Starting speedtest...")

    servers = ['aus.speedtest.sbcglobal.net:8080']

    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    return s.results.dict()


if __name__ == '__main__':
    run()
