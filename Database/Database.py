import mysql.connector
from mysql.connector import errorcode

debug = False

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
		try:
			self.cnx = mysql.connector.connect(**self.config)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				if (debug):
					print("Something is wrong with database username or password")
				return 1
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				if(debug):
					print("Database does not exist")
				return 1
			else:
				if(debug):
					print(err)
				return 1
		else:
			if(debug):
				print('Connected to database: ' + self.config["database"])
			self.cursor = self.cnx.cursor()
			return 0


	def disconnect(self):
		self.cnx.close()
		if(debug):
			print('Disconnected from database: ' + self.config["database"])

	def authenticate(self, username, password):
		self.cursor.execute("select * from users where username = %s", (username,))
		rs = self.cursor.fetchone()
		if (rs == None):
			return 1
		else:
			if (password == rs[1]):
				return 0
