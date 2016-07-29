
from system.core.model import Model
import re

class LoginRegistrationModel(Model):
    def __init__(self):
        super(LoginRegistrationModel, self).__init__()
  
    def create_user(self,info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        # validation
        if not info['first_name'] and not info['last_name']:
            errors.append('Must Enter information in First and Last')
        elif len(info['first_name']) < 2 and len(info['last_name']) < 2:
            errors.append('First or Last Name needs to be atleast 2 charactes long')
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
        else:
            errors.append('Success!')
        if errors:
            return {"status":False, "errors": errors}
        else:
            password = info['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            insert_user = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW()) "
            data = {
                "first_name": info["first_name"],
                "last_name": info["last_name"],
                "email": info['email'],
                "pw_hash": hashed_pw
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
            user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            user_data = {'email':info['email']}

            user = self.db.query_db(user_query, user_data)

            if user:
                if self.bcrypt.check_password_hash(user[0]['password'], password):
                    return { "status": True, "user": user[0] }
            else:
                errors.append('Email does not match')
                return { "status": False, "errors": errors }

        return False
        















