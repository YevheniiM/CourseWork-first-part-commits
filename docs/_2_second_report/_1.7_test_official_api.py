import facebook
from pprint import pprint

ACCESS_TOKEN = 'EAACEdEose0cBAIZBAa7I1RjlsQzyg7qDgWIGDcddE1pVGqm9TZBNMFIMnRaxL6JIYvxmUJVnLc53JitgQoyCa1I2cjWlPdeAXtY2lEOaCT7JMZAZCQXh5P7SG1jaMb1pypV3dqtr0pdcNc3lGKkbAmFGIQ0n36byphE189FCngLgwRLHd0TjucHZBQJFAUcAZD'
graph = facebook.GraphAPI(ACCESS_TOKEN)


def get_friends():
    profile = graph.get_object('me')
    friends = graph.get_connections('me', 'friends')
    pprint(friends)
    friend_list = [friend['name'] for friend in friends['data']]

    return friend_list


def main():
    friends = get_friends()
    pprint(friends)


if __name__ == '__main__':
    main()
