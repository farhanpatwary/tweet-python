import tweepy
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('cfg.py')

consumer_secret = parser.get('twitter_config','consumer_secret')
consumer_key = parser.get('twitter_config','consumer_key')

access_token = parser.get('twitter_config','access_token')
access_token_secret = parser.get('twitter_config','access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status("V3")



