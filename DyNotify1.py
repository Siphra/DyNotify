# DyNotify API test
# Ignore this file, this is my misunderstanding of the question DyNotify2 is the file to use


# libary and resource block

import requests
import os
import tweepy
import facebook

# defined functions block

def tweets(twitterfile,FILENAME,range):
    """  Pulls in twitter API and creates a text from the JSON

    Parameters:
    twitterfile (str) : is the file name where security features are kept

    FILENAME (str) : is the output file name

    range (int) : is the number of tweets to gather

    Returns:
        Text file with tweets, one tweet per line.
    """
    with open(twitterfile):
        api_key = open(twitterfile).readlines()[1][:-1]
        api_secret = open(twitterfile).readlines()[2][:-1]
        token = open(twitterfile).readlines()[4][:-1]
        token_secret = open(twitterfile).readlines()[5][:-1]

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(token, token_secret)
        api=tweepy.API(auth, wait_on_rate_limit = True)

    with open(FILENAME, mode = 'w', encoding = 'utf8') as file:
        twts = tweepy.Cursor(api.search, q = "#gaming", lang = 'en').items(range)
        for tweet in twts:
            file.write(str(tweet))
            file.write('\n')


def faces():


tweets('Twitter.txt','twitterresults.txt', 5)
