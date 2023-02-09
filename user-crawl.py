import tweepy 
import numpy as np 

# read and initialize authentication keys 
with open('auth-keys.txt', 'r') as f: 
    lines = [line.rstrip() for line in f] 
consumer_key, consumer_secret, access_token, access_token_secret = lines[:]

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret)
    
auth.set_access_token(access_token, access_token_secret
    )

# access API 
api = tweepy.API(auth, wait_on_rate_limit=True)

# initialize parameters for limiting users
user_count = 0 
user_dict = dict()
queue = [] 
max_users = 200
max_percent = .05

# initialize the start node as @michaelee
init = 8023702

queue.append(init)

# perform modified BFS for crawling user data 
while queue and user_count < max_users: 

    start_user = queue.pop(0)

    try:   
        # access followers and friends for start node 
        followers_list = api.get_follower_ids(user_id=start_user)
        friends_list = api.get_friend_ids(user_id=start_user)

        # calculate the maximum followers and friends to explore 
        max_following = np.ceil(max_percent*len(followers_list))
        max_friends = np.ceil(max_percent*len(friends_list))
        
        user_following_count_taken = 0
        user_friend_count_taken = 0 

        # explore followers 
        for follower in followers_list: 

            follower_obj = api.get_user(user_id = follower)

            # take only followers with small followings on Twitter 
            if (follower_obj.friends_count > 200) or (follower_obj.followers_count > 200): 
                continue 

            # if new user, add to user dictionary 
            if start_user in user_dict: 
                user_dict[start_user].append(follower) 
            # if previously seen user, update their followers list 
            else: 
                user_dict[start_user] = [follower]
                queue.append(follower)
                user_count += 1

            user_following_count_taken += 1

            # end exploration for this user if we reached the max followers 
            if user_following_count_taken >= max_following: 
                break 
    
        # explore friends 
        for friend in friends_list: 

            friend_obj = api.get_user(user_id = friend)

            # take only friends with small followings on Twitter
            if (friend_obj.friends_count > 200) or (friend_obj.followers_count > 200): 
                continue 
            
            # if friend is a new user, add to user dictionary 
            if friend in user_dict: 
                user_dict[friend].append(start_user)
            # if previously seen, update their followers list 
            else: 
                user_dict[friend] = [start_user]
                queue.append(friend)
                user_count += 1
            
            user_friend_count_taken += 1
            
            # end exploration for this user if we reached the max friends
            if user_friend_count_taken >= max_friends: 
                break 
    
    # skip user if we are unauthorized to access their data 
    except Exception: 
        pass

# write user dictionary to file 
# print(user_count)
# with open('users.txt', 'w') as f:
#     for key, value in user_dict.items(): 
#         f.write('%s|%s\n' %(key, value))