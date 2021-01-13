# DyNotify API test


# libary and resource block

import requests
import tweepy

# defined functions block

def tweets(url,twitterfile,FILENAME):
    response = requests.get(url)
    with open(twitterfile):
    with open(FILENAME), mode = 'a+', encoding = utf8) as file:
        for tweet_id in df1.tweet_id:
             try:
                 temp = api.get_status(tweet_id)
                 json.dump(temp._json, file)
                 file.write('\n')
             except:
               continue



