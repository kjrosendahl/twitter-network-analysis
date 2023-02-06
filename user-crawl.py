import tweepy 
import numpy as np 

# read and init authentication keys 
with open('auth-keys.txt', 'r') as f: 
    lines = [line.rstrip() for line in f] 
consumer_key, consumer_secret, access_token, access_token_secret = lines[:]

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
    )

api = tweepy.API(auth, wait_on_rate_limit=True)

## get_user: returns user object 
# user = api.get_user(screen_name="thekayleedragon")

# # print(user.screen_name)
# print(user.friends_count)
# print(user.followers_count)
# for friend in user.friends(): 
#     print(friend.screen_name)
# for follower in user.followers(): 
#     print(follower.screen_name)

user_count = 0 
user_dict = dict()
queue = [] 
max_users = 5
max_percent = .01

init = api.get_user(screen_name = "michaelee")

queue.append(init)
# queue.append("michaelee")

while queue and user_count < max_users: 

    start_user = queue.pop(0)
    # start_user_name = queue.pop(0)
    # start_user = api.get_user(screen_name=start_user_name)

    max_friends = np.ceil(max_percent*start_user.friends_count)
    max_following = np.ceil(max_percent*start_user.followers_count)
    user_friend_count_taken = 0 
    user_following_count_taken = 0 

    for friend in start_user.friends():
        
        if (friend.friends_count < 500) and (friend.followers_count < 500): 

            # if already discovered user 
            if friend in user_dict: 
                user_dict[friend][0].append(start_user)

            # add to dictionary 
            else: 
                user_dict[friend] = ([start_user], [])
                queue.append(friend)
                user_count += 1 

            user_friend_count_taken += 1
            
        if user_friend_count_taken > max_friends: 
            break
 
    for follower in start_user.followers(): 

        if (follower.friends_count < 500) and (follower.followers_count < 500): 

            if follower in user_dict: 
                user_dict[follower][1].append(start_user)
            else: 
                user_dict[follower] = ([], [start_user])
                queue.append(follower)
                user_count += 1 

            user_following_count_taken += 1 

        if user_following_count_taken > max_following: 
            break
 

# for user in queue: 
#     print(user.screen_name)

# for k, v in user_dict.items(): 
#     print(k, v)

print(len(user_dict))
