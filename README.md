Tools used (can be developed with lower or higher versions): Python 3 Django 1.8 pip 6.0.8 LiClipse 2.1.0.2015

Open as recommended in Eclipse PyDev-Django project, assign the virtualenv as a builder of the project and run the commands for installation with this asset in a console go to the root oauth2ClientPy3 folder and run: pip install - r requirements.txt that installs all the necessary libraries including python-social-auth. (If the administrator user of Django requires is is admin with key admin)

The framework was used python-social-auth for the consumption of Oauth2, implemented or modified 5 components:

- Backend for the provider (Auth2TestBackend):
	Created: Is the component that implements the particularities of the oauth2 (oauth-prov), this directs the customer response authentication.
- Login with oauth-prov (login_button_page.html) Template
	Created: html with a link to login with oauth-prov, associated with the initial url of the user logged in with the authentication provider
- View login with oauth-prov (models)
	Identifies the template to use
- urls
	Modified to include the social-auth url and login view
- settings
	Customized include backend, redirection to send to the provider url, parameters configuration of oauth-prov

The implementation was as follows:
- Auth2TestBackend:
	Extended BaseOAuth2 class implementing the methods: get_user_id, get_user_details, auth_complete_params and user_data and auth_complete and attributes: name, ID_KEY, SCOPE_PARAMETER_NAME, DEFAULT_SCOPE, SCOPE_SEPARATOR, AUTHORIZATION_URL,
ACCESS_TOKEN_URL, RESPONSE_TYPE, STATE_PARAMETER, REDIRECT_STATE, EXTRA_DATA, ACCESS_TOKEN_METHOD

REFERENCES:
Oauth2
 						http://oauth.net/2/
						http://tools.ietf.org/html/rfc6749
						https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
						http://www.bubblecode.net/en/2013/03/10/understanding-oauth2/
						http://www.thegameofcode.com/2012/07/conceptos-basicos-de-oauth2.html
						http://laxmarcaellugar.blogspot.com/2011/08/el-protocolo-de-autenticacion-oauth_08.html

python-social-auth
						http://www.artandlogic.com/blog/2014/04/tutorial-adding-facebooktwittergoogle-authentication-to-a-django-application/		
						https://python-social-auth.readthedocs.org/en/latest/
						https://python-social-auth.readthedocs.org/en/latest/backends/implementation.html
						https://python-social-auth.readthedocs.org/en/latest/configuration/django.html
						http://psa.matiasaguirre.net/docs/backends/implementation.html#oauth2
						https://github.com/omab/python-social-auth/blob/master/social/backends/jawbone.py
						https://github.com/omab/python-social-auth/blob/master/social/backends/google.py
						https://python-social-auth.readthedocs.org/en/latest/backends/google.html#google-oauth2
						https://python-social-auth.readthedocs.org/en/latest/backends/google.html#google-sign-in
						
