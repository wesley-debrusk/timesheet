import mysql.connector
from Database import Database
from mysql.connector import errorcode
from getpass import getpass


db = Database.DB()
code = db.connect()

if (code == 0):
	cursor = db.cnx.cursor()


	print("Username: ", end = " ")
	username = str(input())

	password = getpass()

	print(username + " " + password)


	db.authenticate(username, password)


	db.disconnect()
else:
	print("Could not connect to database.")
