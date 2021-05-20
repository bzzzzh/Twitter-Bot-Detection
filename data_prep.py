import numpy as np
import pandas as pd
import tweepy
import json
import re
import requests
import lxml.html
import sys

CONSUMER_KEY = 'CEop2v3S3TGwYvi1OZeAkBJec'
CONSUMER_SECRET = 'pWkBa0k7YlPcaWFAuMFJKtfX8YwiZtBq84WYX8In9r5yNM1i4J'
ACCESS_TOKEN = '127900998-oj5lSpmfykGKqivkwchT7egHtrNYJJNEqdOrDJUu'
ACCESS_TOKEN_SECRET = 'Hemu3bZO00mKtGtaAXxcepYDg6Qt0GXNVAKBwZrptNN8k'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

twitter_accounts_df = pd.read_csv("twitter_human_bots_dataset.csv", sep=',')
print(f"Dataset shape {twitter_accounts_df.shape}")

df = pd.DataFrame(columns=['id', 'screen_name', 'location', 'description', 'url', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'profile_use_background_image', 'default_profile', 'default_profile_image'])
count = 0

user_list = []

for i in twitter_accounts_df.index:
  try:
    user_info = {}
    print("row# ", i, "/37438", "id: ", twitter_accounts_df["id"][i])
    user = api.get_user(twitter_accounts_df["id"][i])
    user_info['id'] = int(twitter_accounts_df["id"][i])
    user_info['screen_name'] = user.screen_name
    user_info['location'] = user.location
    user_info['description'] = user.description
    user_info['url'] = user.url
    user_info['protected'] = user.protected
    user_info['followers_count'] = int(user.followers_count)
    user_info['friends_count'] = int(user.friends_count)
    user_info['listed_count'] = int(user.listed_count)
    user_info['created_at'] = str(user.created_at)
    user_info['favourites_count'] = int(user.favourites_count)
    user_info['geo_enabled'] = user.geo_enabled
    user_info['verified'] = user.verified
    user_info['statuses_count'] = int(user.statuses_count)
    user_info['lang'] = user.lang
    user_info['profile_use_background_image'] = user.profile_use_background_image
    user_info['default_profile'] = user.default_profile
    user_info['default_profile_image'] = user.default_profile_image

    user_list.append(user_info)
  
  except:
    print("id not found or suspended：", twitter_accounts_df["id"][i])
    #continue

#df.loc[count] = twitter_accounts_df["id"][i] + user.screen_name + user.location + user.description + user.url + user.protected + user.followers_count + user.friends_count + user.listed_count + user.created_at + user.favourites_count + user.geo_enabled + user.verified + user.statuses_count + user.lang + user.profile_use_background_image + user.default_profile + user.default_profile_image
  #count = count + 1

# dump tweets to the file
with open('result.json', 'w') as outfile:
    json.dump(user_list, outfile)
