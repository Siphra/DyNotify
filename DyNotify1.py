# DyNotify API test


# libary and resource block

import requests
import tweepy

# defined functions block

def tweets(url,twitterfile,FILENAME):
    with open(twitterfile):
        api_key = open(twitterfile).readlines()[1].split(':')[1]
        api_secret = open(twitterfile).readlines()[2].split(':')[1]
        token = open(twitterfile).readlines()[4].split(':')[1]
        token_secret = open(twitterfile).readlines()[5].split(':')[1]

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(token, token_secret)
        api=tweepy.API(auth, wait_on_rate_limit = True)

    with open(FILENAME, mode = 'a+', encoding = utf8) as file:
        for tweet_id in df1.tweet_id:
             try:
                 temp = api.get_status(tweet_id)
                 json.dump(temp._json, file)
                 file.write('\n')
             except:
               continue





