import mysql.connector
from mysql.connector import errorcode



class DB:
	def __init__(self):
		self.config = {
		'user': 'root',
		'password': 'databasepass',
		'host': '127.0.0.1',
		'database': 'timesheet',
		'raise_on_warnings': True
		}

	def connect(self):
		self.cnx = mysql.connector.connect(**self.config)
		print('Connected to database: ' + self.config["database"])

	def disconnect(self):
		self.cnx.close()
		print('Disconnected from database: ' + self.config["database"])
