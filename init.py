import tweepy
import json

#YOUR CREDENTIALS
KEY = 
SECRET =
ACCESS_TOKEN = 
ACCESS_TOKEN_SECRET = 

auth = tweepy.OAuthHandler(KEY, SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)



# user = api.get_user('twitter')

# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

# for tweet in api.search(q="Trump", lang="en", count=1):
#       #json_str = json.dumps(tweet._json, indent=4,sort_keys=True)
#       #print(json_str)
#      print(tweet.user_ids)

user = api.get_user(user_id="149534625")
json_str = json.dumps(user._json, indent=4,sort_keys=True)
print(json_str)

# for user in api.get_user(user_id="149534625"):
#        json_str = json.dumps(user._json, indent=4,sort_keys=True)
#        print(json_str)
# Bellow checks for the UK trends
# for trends in api.trends_place('23424975'):
#   parsed = json.loads(trends)
#   print(json.dumps(parsed, indent=4, sort_keys=True))
#    #print(trends)