from instagram.client import InstagramAPI


def access(token, secret):
    access_token = token
    client_secret = secret
    return InstagramAPI(access_token=access_token, client_secret=client_secret)


def main():
    api = access("938353142.a04429e.8e57ff24cebe45118e13a7ffef57781f",
                 "49892dd15d3743e3baea402eb6a91208")

    from pprint import pprint

    media = api.user_liked_media("938353142")
    pprint(media)

    for m in media[0]:
        if api.media_comments(m.id):
            for comment in api.media_comments(m.id):
                print('comment -> ' + str(comment.text))


if __name__ == '__main__':
    main()
