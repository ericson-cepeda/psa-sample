'''
Created on 29/05/2015

@author: jorge.martinez
'''
from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.utils.http import urlencode
from social.backends.oauth import BaseOAuth2
from social.utils import handle_http_errors

from oauth2ClientPy3.settings import OAUTH2TEST_ENDPOINT


class TestOAuth2(BaseOAuth2):
    """Test OAuth authentication backend"""
    # Oauth params
    name = 'oauth2test'
    ID_KEY = 'id'
    SCOPE_PARAMETER_NAME = 'scope'
    DEFAULT_SCOPE = None
    SCOPE_SEPARATOR = ' '
    
    REQUIRES_EMAIL_VALIDATION = False
    EXTRA_DATA = None
    
    # Oauth2 params
    AUTHORIZATION_URL = OAUTH2TEST_ENDPOINT+'/AuthEndpoint'
    ACCESS_TOKEN_URL  = OAUTH2TEST_ENDPOINT+'/TokenEndpoint'
    RESPONSE_TYPE = 'code'
    STATE_PARAMETER = True
    REDIRECT_STATE = False
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires')
    ]
    ACCESS_TOKEN_METHOD = 'POST'
    
    #parametros exclusivos de TestOAuth2
    USER_RESOURCE_URL = OAUTH2TEST_ENDPOINT+'/api/v1/user/me?'
    
    def get_user_id(self, details, response):
        return response['id']

    def get_user_details(self, response):
        """Return user details from Test account"""
        return {'username': response.get('login') or 'test_login' ,
                'email': response.get('email') or 'test_email',
                'first_name': response.get('name') or "test_name",
                'id': response.get('id') or "test_id",
                }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = self.USER_RESOURCE_URL + urlencode({
            'access_token': access_token
        })
        # return json.load(self.urlopen(url))
        data = self.get_json(url)
        return data
        
    def auth_complete_params(self, state=None):
        client_id, client_secret = self.get_key_and_secret()
        return {
            'grant_type': 'authorization_code',  # request auth code
            'code': self.data.get('code', ''),  # server response code
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri' : LOGIN_REDIRECT_URL,
            }
    
    @handle_http_errors
    def auth_complete(self, *args, **kwargs):
        """Completes loging process, must return user instance"""
        self.process_error(self.data)
        response = self.request_access_token(
            self.ACCESS_TOKEN_URL,
            params=self.auth_complete_params(self.validate_state()),
            headers=self.auth_headers(),
            method=self.ACCESS_TOKEN_METHOD
        )
        self.process_error(response)
        return self.do_auth(response['access_token'], response=response, *args, **kwargs)