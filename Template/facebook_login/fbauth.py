"""
Ex:

import fbauth

fbAuth = fbauth.TokenHandler(os.environ['FB_APP_ID'],
                os.environ['FB_APP_SECRET'])

access_token = fbAuth.get_access_token()
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen, HTTPError
from webbrowser import open_new


class FacebookAuthorization:
    REDIRECT_URL = 'http://localhost:8080/'
    PORT = 8080
    access_token = ''

    def __init__(self, application_key, application_secret):
        token_handler = self.TokenHandler(application_key, application_secret)
        token_handler.get_access_token()

    class HTTPServerHandler(BaseHTTPRequestHandler):
        """
        HTTP Server callbacks to handle Facebook OAuth redirects

        """
        def __init__(self, request, address, server, a_id, a_secret):
            self.app_id = a_id
            self.app_secret = a_secret
            super().__init__(request, address, server)

        def do_GET(self):
            graph_api_auth_uri = (
                                  'https://graph.facebook.com/v2.2/oauth/acc'
                                  'ess_token?client_id={0}&redirect_uri={1}&'
                                  'client_secret={2}&code='.format(
                                        self.app_id,
                                        FacebookAuthorization.REDIRECT_URL,
                                        self.app_secret
                                        )
                                  )

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if 'code' in self.path:
                self.auth_code = self.path.split('=')[1]
                self.wfile.write(bytes('<html><h1>You may now close this window.'
                                  + '</h1></html>', 'utf-8'))
                FacebookAuthorization.access_token = self.appropriate_token(
                    FacebookAuthorization.get_access_token_from_url(
                        graph_api_auth_uri + self.auth_code
                    )
                )

        @staticmethod
        def appropriate_token(string):
            token = string.split(':')[1].replace('"', '').split(',')[0]
            return token

        # Disable logging from the HTTP Server
        def log_message(self, format, *args):
            return

    class TokenHandler:
        """
        Functions used to handle Facebook oAuth

        """
        def __init__(self, a_id, a_secret):
            self._id = a_id
            self._secret = a_secret

        def get_access_token(self):
            """
             Fetches the access key using an HTTP server to handle oAuth
             requests
                Args:
                    appId:      The Facebook assigned App ID
                    appSecret:  The Facebook assigned App Secret
            """

            ACCESS_URI = ('https://www.facebook.com/dialog/'
                + 'oauth?client_id=' +self._id + '&redirect_uri='
                + FacebookAuthorization.REDIRECT_URL + "&scope=ads_management")

            open_new(ACCESS_URI)
            httpServer = HTTPServer(
                    ('localhost', FacebookAuthorization.PORT),
                    lambda request, address, server: FacebookAuthorization.HTTPServerHandler(
                        request, address, server, self._id, self._secret))
            httpServer.handle_request()

    @staticmethod
    def get_access_token_from_url(url):
        """
        Parse the access token from Facebook's response
        Args:
            uri: the facebook graph api oauth URI containing valid client_id,
                 redirect_uri, client_secret, and auth_code arguements
        Returns:
            a string containing the access key

        """
        access_token = str(urlopen(url).read(), 'utf-8')
        return access_token
