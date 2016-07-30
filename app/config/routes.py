
from system.core.router import routes


routes['default_controller'] = 'Users'


routes['POST']['/users/create'] = "Users#create"
routes['POST']['/user/login'] = "Users#login_user"
routes['GET']['/success'] = "Users#success"
routes['GET']['/destination/<int:id>'] = "Users#destination"
routes['GET']['/addtrip'] = "Users#addtrip"
routes['/logout'] = "Users#logout"
routes['POST']['/inserttrip/<int:id>'] = "Users#add"
routes['POST']['/join/<int:id>'] = "Users#join"











