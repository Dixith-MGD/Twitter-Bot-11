import tweepy
from time import sleep

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def send_dm(user_id, message):
    try:
        api.send_direct_message(user_id, text=message)
        print(f"DM sent to user with ID: {user_id}")
    except tweepy.TweepError as e:
        print(f"Failed to send DM to user with ID: {user_id}")
        print(f"Error: {str(e)}")

def get_followers(user_id):
    followers = []
    try:
        for follower in tweepy.Cursor(api.followers_ids, id=user_id).items():
            followers.append(follower)
        return followers
    except tweepy.TweepError as e:
        print(f"Failed to retrieve followers for user with ID: {user_id}")
        print(f"Error: {str(e)}")
        return []

target_user_id = 'TARGET_USER_ID'
message = 'Hey there! Check out our awesome Instagram pages!'

followers = get_followers(target_user_id)
for follower_id in followers:
    send_dm(follower_id, message)
    sleep(1)  # Be a bit slow to avoid getting caught too quickly
