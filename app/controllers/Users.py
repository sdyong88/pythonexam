
from system.core.controller import *


class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
    
        self.load_model('UsersModel')
        self.load_model('TripsModel')
        self.db = self._app.db

    def index(self):

        return self.load_view('/users/index.html')

    def success(self):
        alltrips = self.models['TripsModel'].show_all_trips()
        usertrips = self.models['TripsModel'].show_user_trips(session['user']['user_id'])
        return self.load_view('/users/travels.html', user = session['user'], trips = alltrips, mytrip = usertrips)

    def addtrip(self):
        return self.load_view('/users/addtrip.html', user = session['user'])

    def destination(self,id):
        info = self.models['TripsModel'].show_destination(id)
        joins = self.models['TripsModel'].join_trip(id)
        return self.load_view('/users/destination.html', infos = info, joins = joins)

    def logout(self):
    	session.clear()
    	return redirect('/')

    def create(self):
        user_info = {
            "name": request.form['name'],
            "alias": request.form['alias'],
            "email": request.form['email'],
            "password": request.form['password'],
            "confirm_pw": request.form['confirm_pw']
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
            'destination':request.form['destination'],
            'description': request.form['description'],
            'start':request.form['start_time'],
            'finish': request.form['end_time'],
            'id': id
        }
        self.models['TripsModel'].add_trip(data)
        print "insert successful"
        return redirect('/success')

    def join(self, id):
        data = {
            "trip_id": id,
            "user_id": session['user']['user_id']
        }
        self.models['TripsModel'].add_favorite(data)

        return redirect('/success')







