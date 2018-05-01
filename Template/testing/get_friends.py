import facebook
from pprint import pprint
from facebook_login import fbauth

# user = fbauth.FacebookAuthorization('230738837471197', '6f244796a41e02a89581e0730bbdad70')
#
# ACCESS_TOKEN = user.access_token
ACCESS_TOKEN = 'EAADR2xJxf90BAPyeZAsZCjn3TOxwFw9mXoc3NNevZCTh3mFovTAsEiZCnyz6J08WZBGkXLmhXiZCxAficHBbeRTXmBbfrMn8qXc4E0jZA1BzhuJYqi4a2jlbGq4XFycwc6Go67Mma8dNXLlNL2v7mst19YrMPLjlBoqFbJUQ9vD8AZDZD'
graph = facebook.GraphAPI(ACCESS_TOKEN)
print(ACCESS_TOKEN)


def get_friends():
    profile = graph.get_object('me')
    pprint(profile)
    friends = graph.get_connections('me', 'friends')
    pprint(friends)
    friend_list = [friend['name'] for friend in friends['data']]

    return friend_list


def main():
    friends = get_friends()
    pprint(friends)


if __name__ == '__main__':
    main()
