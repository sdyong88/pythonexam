from system.core.model import Model
import re

class TripsModel(Model):
    def __init__(self):
        super(TripsModel, self).__init__()

    def add_trip(self,info):
    	#validation
    	query = "INSERT INTO trips (destination, description, start, finish, created_at, updated_at, user_id) VALUES (:destination, :description, :start, :finish, NOW(), NOW(), :user_id) "

    	data = {
    		'destination':info['destination'],
    		'description': info['description'],
    		'start': info['start'],
    		'finish': info['finish'],
    		'user_id': info['id']
    	}
    	self.db.query_db(query,data)

    def show_all_trips(self):
    	query = "SELECT users.name, users.id, trips.id AS trip_id, trips.destination, trips.start, trips.finish FROM users LEFT JOIN trips ON users.id = trips.user_id"
    	return self.db.query_db(query)

    def add_favorite(self,info):
    	query = "INSERT INTO planned (user_id, trip_id) VALUES (:user_id, :trip_id)"
    	data = {
    		'user_id':info['user_id'],
    		'trip_id':info['trip_id']
    	}
    	self.db.query_db(query,data)
    
    def show_user_trips(self,info):
    	query ="SELECT users.id AS user_id, trips.destination AS destination, trips.start AS start, trips.finish AS finish, trips.description AS description FROM users LEFT JOIN planned ON users.id = planned.user_id LEFT JOIN trips ON trips.id = planned.trip_id WHERE users.id = :user_id"
    	data = {'user_id':info }
    	print data
    	return self.db.query_db(query,data)

    def show_destination(self,info):
    	query = "SELECT * FROM trips LEFT JOIN users ON users.id = trips.user_id WHERE trips.id = :id"
    	data = {'id': info}
    	return self.db.query_db(query, data)

    def join_trip(self,info):
    	query = "SELECT * FROM planned LEFT JOIN users ON users.id = planned.user_id WHERE trip_id =:trip_id"
    	data = {'trip_id':info}
    	return self.db.query_db(query,data)