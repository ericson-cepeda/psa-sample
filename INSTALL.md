**Installation from the oauth2 supplier**
Upload the oauth-prov.war on a tomcat 6 + with a JDK 6

**Oauth2 consumer installation**
Please create a virtualenv and run Setup with this active commands. In a console go to the root folder oauth2ClientPy3 and run:
- PIP install - r requirements.txt
- Python manage.py runserver


**Test:**
	- In the browser to activate the console go to http://127.0.0.1: 8000/login
	- Click on start with oauth2test
		- oauth2ClientPy3 redirects to oauth-prov by sending the state
 		- Gets the access token
		- Session begins and http://127.0.0.1 page appears: 8000/main

If activated the browser console, on the tab network will look as follows:
	
	┌───────────┬────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
	│ RESPUESTA │ METODO │ URL                                                                                                                                                                                 │
	├───────────┼────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
	│ 200 OK    │  GET   │ "http://127.0.0.1:8000/login"                                                                                                                                                       │
	│ 302 FOUND │  GET   │ "http://127.0.0.1:8000/login/oauth2test/?next=/main"                                                                                                                                │
	│ 302 FOUND │  GET   │ "http://127.0.0.1:8080/oauth-prov/AuthEndpoint?response_type=code&client_id=TestKey&redirect_uri=http://127.0.0.1:8000/complete/oauth2test/&state=vkTqtm0EsOj8E5oTDg5bGMabIgl172A0" │
	│ 302 FOUND │  GET   │ "http://127.0.0.1:8000/complete/oauth2test/?state=vkTqtm0EsOj8E5oTDg5bGMabIgl172A0&code=f1b7f3f83aff12a9ad2c0eb2ca289992"                                                           │
	│ 200 OK    │  GET   │ "http://127.0.0.1:8000/main"                                                                                                                                                        │
	└───────────┴────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘	
	
