import tweepy 

# read and init authentication keys 
with open('auth-keys.txt', 'r') as f: 
    lines = [line.rstrip() for line in f] 
consumer_key, consumer_secret, access_token, access_token_secret = lines[:]

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
    )

api = tweepy.API(auth)

# user = api.get_user(screen_name="thekayleedragon")

# print(user.screen_name)
# print(user.friends_count)
# for friend in user.friends(): 
#     print(friend.screen_name)