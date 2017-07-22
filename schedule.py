"""
Background scheduler to schedule yellowcard.py execution on 5 min
intervals.
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


def schedule_run(func_to_run, mins):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func_to_run, 'interval', minutes=mins)
    scheduler.start()
    print("Interval: {} min(s)".format(mins))
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'), flush=True)

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()