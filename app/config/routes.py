
from system.core.router import routes


routes['default_controller'] = 'Users'


routes['POST']['/users/create'] = "Users#create"
routes['POST']['/user/login'] = "Users#login_user"
routes['GET']['/success'] = "Users#success"
routes['/logout'] = "Users#logout"
routes['POST']['/addqoute/<int:id>'] = "Users#add"
routes['/user/<int:id>'] = "Users#show"
routes['POST']['/add_favorite/<int:id>'] = "Users#addqoute"
routes['POST']['/delete/<int:id>'] = "Users#delete"










