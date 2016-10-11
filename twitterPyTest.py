# -*- encoding: utf-8 -*-
from twitter import *

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""


#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#-----------------------------------------------------------------------
# request my home timeline
# twitter API docs: https://dev.twitter.com/docs/api/1/get/statuses/home_timeline
#-----------------------------------------------------------------------
statuses = twitter.statuses.home_timeline(count = 50)

#-----------------------------------------------------------------------
# loop through each of my statuses, and print its content
#-----------------------------------------------------------------------
for status in statuses:
    print "(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"])
