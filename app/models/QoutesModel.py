from system.core.model import Model
import re

class QoutesModel(Model):
    def __init__(self):
        super(QoutesModel, self).__init__()
  
 	def show_qoutes(self):
 		query = "SELECT users.id, users.name, users.password, qoutes.author, qoutes.qoute, favorites.qoute_id FROM users LEFT JOIN qoutes ON users.id = qoutes.user_id LEFT JOIN favorites on qoutes.id = favorites.qoute_id;"
 		return self.db.query_db(query)