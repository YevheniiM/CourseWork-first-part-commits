import json
from requests import get

api_key = "938353142.a04429e.8e57ff24cebe45118e13a7ffef57781f"


def get_user_id(username):
    answer = get('https://api.instagram.com/v1/users/search?q=' + username + '&access_token=' + api_key,
                 verify=True).json()
    if answer['data']:
        return answer['data'][0]['id']


def get_media(username):
    user_id = get_user_id(username)
    json_file = get('https://api.instagram.com/v1/users/' + user_id +
                    '/media/recent/?access_token=' + api_key,
                    verify=True).json()
    data = json_file['data']
    data_list = list()

    for post in data:
        final_dict = dict()
        final_dict['filter'] = post['filter']
        if post['caption']:
            final_dict['caption'] = post['caption']['text']
        final_dict['likes'] = post['likes']['count']
        if post['location']:
            final_dict['location'] = post['location']['name']
        data_list.append(final_dict)

    return data_list


def get_users_from_json(data_input):
    data_answer = list()
    for i in range(len(data_input[u'data'])):
        data_answer.append(data_input[u'data'][i][u'username'])
    return data_answer


def print_media(username):
    """Prints users by their last posts locations

    """
    media = get_media(username)
    for post in media:
        print('-------------------------------------------')
        print('Likes on the post: ' + str(post['likes']))
        if 'location' in post:
            print('Post location    : ' + post['location'])
        if 'caption' in post:
            print('Post caption     : ' + post['caption'])
        print('-------------------------------------------\n')


if __name__ == '__main__':
    print_media("evgesh_m")

