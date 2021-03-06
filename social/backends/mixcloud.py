"""
Mixcloud OAuth2 support
"""
from social.backends.oauth import BaseOAuth2


class MixcloudOAuth2(BaseOAuth2):
    name = 'mixcloud'
    ID_KEY = 'username'
    AUTHORIZATION_URL = 'https://www.mixcloud.com/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://www.mixcloud.com/oauth/access_token'

    def get_user_details(self, response):
        return {'username': response['username'],
                'email': None,
                'fullname': response['name'],
                'first_name': None,
                'last_name': None}

    def user_data(self, access_token, *args, **kwargs):
        try:
            return self.get_json('https://api.mixcloud.com/me/', params={
                'access_token': access_token,
                'alt': 'json'
            })
        except (ValueError, KeyError, IOError):
            return None
