import tweepy
import os

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
USER_ID = os.getenv("USER_ID")

def run():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                          )
    
    follower=client.get_users_followers(USER_ID)
    try:
        for user in follower.data:
            client.block(user.id)
            client.unblock(user.id)
            print(user.username+" remove")
    except TypeError:
        print("no follower")
print("start")
