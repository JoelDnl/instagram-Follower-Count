from instagrapi import Client

def main():


    # Reads cred.txt file...
    with open ("cred.txt", "r") as f:
        username, password = f.read().splitlines()

    client = Client()
    client.login(username, password, verification_code="<2F Authentication Number>")
    
    # If there is no 2FA, then use this:
    #client.login(username, password)

    # Get followers
    followers = client.user_followers(client.user_id_from_username(username))
    
    # To print out all followers
    #####################
    #print("Followers:")
    #for user_id in followers:
    #    print(followers[user_id].username)
    #####################


    # Get following
    following = client.user_following(client.user_id_from_username(username))

    # To print out all following
    #####################
    #print("\nFollowing:")
    #for user_id in following:
    #    print(following[user_id].username)
    #####################

    # Convert to sets for easier comparison
    followers_set = set(followers.keys())
    following_set = set(following.keys())

    # Find users you follow who don't follow you back
    not_following_back = following_set - followers_set
    print("Users I'm following but who don't follow me back:")
    for user_id in not_following_back:
        print(following[user_id].username)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Find users who follow you but you don't follow back
    not_followed_by_me = followers_set - following_set
    print("\nUsers who follow me but I don't follow back:")
    for user_id in not_followed_by_me:
        print(followers[user_id].username)

if __name__ == '__main__':
    main()
