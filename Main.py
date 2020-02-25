import mysql.connector
import Connect
from mysql.connector import errorcode


# config = {
# 'user': 'root',
# 'password': 'databasepass',
# 'host': '127.0.0.1',
# 'database': 'timesheet',
# 'raise_on_warnings': True
# }
#
# try:
# 	cnx = mysql.connector.connect(**config)
# except mysql.connector.Error as err:
# 	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
# 		print("Something is wrong with your user name or password")
# 	elif err.errno == errorcode.ER_BAD_DB_ERROR:
# 		print("Database does not exist")
# 	else:
# 		print(err)
# else:
# 	print("success")
#
# 	cursor = cnx.cursor()
# 	cursor.execute("select * from users")
# 	for (username, password) in cursor:
#   		print(username, password)
# 	cursor.close()
#
#
# 	cnx.close()

db = Connect.DB()
db.connect()
