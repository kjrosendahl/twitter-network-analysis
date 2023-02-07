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
max_users = 30
max_percent = .02

init = 8023702

# init = api.get_user(screen_name = "michaelee")

# print(init.id)

queue.append(init)

while queue and user_count < max_users: 

    start_user = queue.pop(0)
    print(start_user)
    followers = api.get_follower_ids(user_id = start_user)
    friends = api.get_friend_ids(user_id = start_user)
    # followers.sort() 
    # friends.sort() 

    max_following = np.ceil(max_percent*len(followers))
    max_friends = np.ceil(max_percent*len(friends))

    print(len(followers), len(friends), max_following, max_friends)

    user_following_count_taken = 0
    user_friend_count_taken = 0 

    for fol in followers: 

        follower_obj = api.get_user(user_id = fol)
        if (follower_obj.friends_count > 200) or (follower_obj.followers_count > 200): 
            continue 

        if fol in user_dict: 
            user_dict[fol][1].append(start_user) 
        else: 
            user_dict[fol] = ([], [start_user])
            queue.append(fol)
            user_count += 1
        
        user_following_count_taken += 1
        if user_following_count_taken > max_following: 
            break 
 
    for fr in friends: 

        friend_obj = api.get_user(user_id = fr)
        if (friend_obj.friends_count > 200) or (friend_obj.followers_count > 200): 
            continue 
        
        if fr in user_dict: 
            user_dict[fr][0].append(start_user)
        else: 
            user_dict[fr] = ([start_user], [])
            queue.append(fr)
            user_count += 1
        
        user_friend_count_taken += 1
        if user_friend_count_taken > max_friends: 
            break 

# for user in queue: 
#     print(user.screen_name)
print(user_count)
with open('users.txt', 'w') as f:
    for key, value in user_dict.items(): 
        f.write('%s %s\n' %(key, value))