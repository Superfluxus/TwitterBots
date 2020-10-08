#!/usr/bin/env python
import sys
import os
import datetime
from twython import Twython
import math
import pprint

#Get current time
currenthour=datetime.datetime.now().hour
currentminute=datetime.datetime.now().minute


if currentminute > 15:
    print ("Minute is past 15, exit")
    sys.exit()

#Define API Variables
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
checker=api.show_user(screen_name="")
current = checker['status']
full = current['created_at']
hour1 = full[11:13]
hour1 = int(hour1) + 1 
print(hour1)

if hour1 == currenthour:
    sys.exit()

now = datetime.datetime.now()
tweet=api.show_user(screen_name='big_ben_clock')
latest = tweet['status']
time = latest['created_at']
tweetid = latest['id']
fulltime = time[11:19]
year = time[26:30]
month = time[4:7]
hour = time[11:13]
hour = int(hour) + 1
if hour == 24:
   hour = 0
day = time[4:6]
minute = time[14:16]
second = time[17:19]

if hour == currenthour:
    print("Tweeting...")  
    import ""
else:
   print("Conditions not met")
