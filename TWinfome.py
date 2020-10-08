
#!/usr/bin/env python
import sys
import os
import datetime
from twython import Twython
import math
import pprint

#Define our constant variables
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

tweets = api.get_mentions_timeline(count=5)


checker = api.get_user_timeline(screen_name='', count=50)

counter = 0
for item in tweets:
    counter += 1
    print("We're starting run number " + str(counter))
    actioned = False
    text = item['text']
    text = text.lower()
    if "#twinfome" in text:
        print("Valid request found, have we already tweeted them?")
    else:
        print("Not looking for an action, disregard")
        continue

    tweetid = item['id']

    for tweet in checker:
          id = tweet['in_reply_to_status_id']
          if id == tweetid:
                   print("I already tweeted this guy!")
                   print("I have replied to " + str(tweetid) + " with my reply of " + str(id))
                   actioned = True                   
                   break
          else:
                   print("This tweet wasn't a match, continue looking...")
                   print('#DEBUG = Their tweet of ID: ' + str(tweetid) + "did not match my reply of " + str(id) )
                   continue
    if actioned == True:
        continue
    elif actioned == False:
        print("Somebody has tweeted me with hashtag and I have not tweeted them back")
        print("#DEBUG - Their tweet ID was " + str(tweetid) )
        actioned = "N/A"
        userid = item['user']['id']
        user = api.show_user(id=userid)
        created=user['created_at']
        likes=user['favourites_count']
        followers=user['followers_count']
        following=user['following']
        lists=user['listed_count']
        username=user['screen_name']
        tweets=user['statuses_count']
        created = created[0:19] + " " + created[26:30]
        tweets = str(tweets)
        lists = str(lists)
        likes = str(likes)        
        One = "Hello " + "@" +(username)
        Two = "Here are your stats:"
        Three = "Your account was created on " + (created)
        Four = "You have tweeted " + (tweets) + " times"
        Five = "You are a part of " + (lists) + " different lists"
        Six = "You have favourited " + (likes) + " tweets"
        string = (One) +"\n" + (Two) + "\n" + "\n" + (Three) +"\n" + (Four) + "\n" + (Five) +"\n" + (Six) + "\n"
        print("TWEETING NOW!!")
        api.update_status(status=string, in_reply_to_status_id =tweetid)

print("All tweets checked, no work to do, script complete")


