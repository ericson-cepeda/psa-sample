Herramientas usadas (Se puede desarrollar con versiones inferiores o superiores):
	Python 3
	Django 1.8
	pip 6.0.8
	LiClipse 2.1.0.2015

Abrir como proyecto PyDev-Django en Eclipse,
Se recomienda asignar el virtualenv como builder del proyecto y ejecutar los comandos de instalación con este activo
En una consola ir a la carpeta raíz oauth2ClientPy3 y ejecutar:
	pip install -r requirements.txt
	Esto instala todas las librerias necesarias incluyendo python-social-auth.
	(Si se requiere el usuario administrador de Django es admin con clave admin)

Se utilizó el framework python-social-auth para el consumo de Oauth2, se implementaron o modificaron 5 componentes:

	- Backend para el proveedor (Auth2TestBackend): 
		Creado: Es el componente que implementa las particularidades del proveedor de oauth2 (oauth-prov), este le 
		dirige al cliente la respuesta de autenticación.
	- Template de login con oauth-prov(login_button_page.html)
		Creado: html con el link para iniciar sesión con oauth-prov, asocia la url inicial del usuario logeado con
		el proveedor de autenticación
	- Vista de login con el oauth-prov (models)
		Identifica el template a usar
	- urls
		Modificado para incliur las url de social-auth y la de la vista de login
	- settings
		Modificado para incliur el backend, la url de redirección para enviarle al proveedor, los parámetros 
		de configuración de oauth-prov
	
	Para la implementación se realizó lo siguiente:
		- Auth2TestBackend:
			Se extendió la clase BaseOAuth2 implementando los métodos:
				get_user_id, get_user_details, user_data, auth_complete_params y auth_complete
			y los atributos:
				name, ID_KEY, SCOPE_PARAMETER_NAME, DEFAULT_SCOPE, SCOPE_SEPARATOR, AUTHORIZATION_URL, 
				ACCESS_TOKEN_URL, RESPONSE_TYPE, STATE_PARAMETER, REDIRECT_STATE, EXTRA_DATA, ACCESS_TOKEN_METHOD
				
REFERENCIAS:
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
						