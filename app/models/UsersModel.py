
from system.core.model import Model
import re

class UsersModel(Model):
    def __init__(self):
        super(UsersModel, self).__init__()
  
    def create_user(self,info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        # validation
        if not info['name'] and not info['alias']:
            errors.append('Must Enter information in Name and Alias')
        elif len(info['name']) < 2 and len(info['alias']) < 2:
            errors.append('Name and Alias needs to be atleast 2 charactes long')
        if not info['email']:
            errors.append('Email cannot be blank**')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format is invalid**')
        if not info['password']:
            errors.append('Password cannot be blank**')
        elif len(info['password']) < 7:
            errors.append('Password needs be atleast 8 characters long**')
        elif info['password'] != info['confirm_pw']:
            errors.append('Password and Confirmation do not match! **')
        if not info['birthdate']:
        	errors.append('D.O.B was not selected')
        # else:
        #     errors.append('Success!')
        if errors:
            return {"status":False, "errors": errors}
        else:
            password = info['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            insert_user = "INSERT INTO users (name, alias, email, password, birthdate, created_at) VALUES (:name, :alias, :email, :pw_hash, :birthdate, NOW()) "
            data = {
                "name": info["name"],
                "alias": info["alias"],
                "email": info['email'],
                "pw_hash": hashed_pw,
                "birthdate": info['birthdate']
            }
            self.db.query_db(insert_user,data)

            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0]}


    def login_check(self, info):
        errors = []
        if not info['email']:
            errors.append('Email cannot be blank**')
        elif len(info['password']) < 7:
            errors.append('Password needs be atleast 8 characters long**')

        if errors:
            return {"status": False, "errors": errors}
        else:
            password = info['password']  
            user_query = "SELECT users.id AS user_id, users.name , users.password FROM users WHERE email = :email LIMIT 1"
            user_data = {'email':info['email']}

            user = self.db.query_db(user_query, user_data)



        if self.bcrypt.check_password_hash(user[0]['password'], password):
            return { "status": True, "user": user[0] }
        else:
            errors.append('Email and/or Password does not match')
            return { "status": False, "errors": errors }

    def add_qoute(self,info):
    	query = "INSERT INTO qoutes(qoute, author, created_at, user_id) VALUES (:qoute, :author, NOW(), :user_id)"

    	data = {
    		'qoute':info['qoute'],
    		'author': info['author'],
    		'user_id': info['user_id']
    	}
    	self.db.query_db(query, data)

    def show_favorite(self,info):
 		query = "SELECT *,favorites.id as favorite_id FROM favorites LEFT JOIN qoutes ON qoutes.id = favorites.qoute_id WHERE favorites.user_id = :users_id"
 		data = {'users_id': info}
 		return self.db.query_db(query,data)

    def insert(self, info):
 		query = "INSERT INTO favorites (qoute_id, user_id) VALUES (:qoute_id, :user_id)"
 		data = {'qoute_id': info['id'], 'user_id': info['user_id']}
 		self.db.query_db(query,data)

    def delete(self,info):
        query = "DELETE FROM favorites WHERE favorites.id = :qoute_id"
        data = {'qoute_id': info['id']}
        self.db.query_db(query,data)

    def show(self, info):
 		query = "SELECT * FROM users LEFT JOIN qoutes ON users.id = qoutes.user_id WHERE users.id = :id"
 		data = { 'id': info}
 		return self.db.query_db(query,data)

    def show_qoutes(self):
 		query = "SELECT * FROM qoutes LEFT JOIN users ON users.id = qoutes.user_id"
 		return self.db.query_db(query)




 	
        
        















