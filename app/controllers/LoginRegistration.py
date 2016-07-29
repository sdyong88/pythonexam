
from system.core.controller import *


class LoginRegistration(Controller):
    def __init__(self, action):
        super(LoginRegistration, self).__init__(action)
    
        self.load_model('LoginRegistrationModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def success(self):
        return self.load_view('success.html', users = session['first_name'])


    def create(self):
        user_info = {
            "first_name": request.form['fname'],
            "last_name": request.form['lname'],
            "email": request.form['email'],
            "password": request.form['password'],
            "confirm_pw": request.form['confirm_pw']
        }
        create_status = self.models['LoginRegistrationModel'].create_user(user_info)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
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

        user_login = self.models['LoginRegistrationModel'].login_check(data)
        
        if user_login['status'] == True:
            session['first_name'] = user_login['user']['first_name']
            return redirect('/success')
        else:
            for message in user_login['errors']:
                flash( message, "regis_error")
            return redirect('/')

    

