import os
import tweepy as tw
import pandas as pd


consumer_key= "fGPBFApBYFQqFeNkjrbYkOD2Q"
consumer_secret= 'jJxIAM83c6qO1SUz7uW2rM6DRHP625FGQmYONyf18sGpMGTEEJ'
access_token= '711490908353654785-3MWudri9PefUKnivW946MZ7VN8k2ZiG'
access_token_secret= 'U9MIVLvaKz0lSCUqxvheFxABt6zU7zeLvQfdgA0Ki355N'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
BT = "AAAAAAAAAAAAAAAAAAAAAKE1WgEAAAAAPlLnvjzbgSh9JSGbo%2FQvoT5zSEQ%3DTn9SgxdAKEVyBbQQIS7UVLU6ac9rBfY1mH3zf3PuwVkgXC8oNZ"




def getTweets(a, b):
    # Collect tweets
    # Collect tweets
    tweets = tw.Cursor(api.search_tweets,
                q=a,
                lang="en",
                since=b, 
                place_country="KE"
                ).items()
    for tweet in tweets:
        return tweet.text
    return tweets
