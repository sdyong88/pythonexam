
from system.core.controller import *


class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
    
        self.load_model('UsersModel')
        self.load_model('QoutesModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('/users/index.html')

    def success(self):
    	qoutes = self.models['UsersModel'].show_qoutes()
    	favorites = self.models['UsersModel'].show_favorite(session['user']['user_id'])
        return self.load_view('/users/success.html', users = session['user'], shows = qoutes, favorites = favorites)

    def logout(self):
    	session.clear()
    	return redirect('/')

    def create(self):
        user_info = {
            "name": request.form['name'],
            "alias": request.form['alias'],
            "email": request.form['email'],
            "password": request.form['password'],
            "confirm_pw": request.form['confirm_pw'],
            "birthdate": request.form['birthdate']
        }
        create_status = self.models['UsersModel'].create_user(user_info)

        if create_status['status'] == True:
            # session['id'] = create_status['user']['id']
            return redirect('/')
        else:
            for message in create_status['errors']:
                flash(message, "regis_error")
            return redirect('/')
        
    def login_user(self):
        data = {
            "email":request.form['log_email'],
            "password": request.form['password']
        }

        user_login = self.models['UsersModel'].login_check(data)
        
        if user_login['status'] == True:
            session['user'] = user_login['user']
            print session['user']
            
            return redirect('/success')
        else:
            for message in user_login['errors']:
                flash( message, "regis_error")
            return redirect('/')

    def add(self,id):
    	data = {
    		'qoute': request.form['qoute'],
    		'author': request.form['author'],
    		'user_id': id
    	}
    	print data
    	self.models['UsersModel'].add_qoute(data)
    	print "it has been posted"
    	return redirect('/success')
    
    def show(self,id):
    	print "it got to show"
    	qoutes = self.models['UsersModel'].show(id)
    	self.models['UsersModel'].show_qoutes()
    	return self.load_view('/users/show.html', qoutes = qoutes)
   
    
    def addqoute(self,id):
    	print "adding favorite"
    	data = {'id': id, 'user_id':session['user']['user_id']}
    	self.models['UsersModel'].insert(data)
    	return redirect('/success')

    def delete(self,id):
        data = {'id':id}
        print data
        self.models['UsersModel'].delete(data)
        return redirect('/success')








