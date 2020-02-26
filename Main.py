import mysql.connector
import os
import App
from Database import Database
from mysql.connector import errorcode
from getpass import getpass

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("-----Timesheet Tracker-----")

clear_screen()


# Connect to database
db = Database.DB()
dbcode = db.connect()
if (dbcode == 0):
	cursor = db.cnx.cursor()

app = App.Timesheet(cursor)

while (True):
	print("Username: ", end = " ")
	username = str(input())
	password = getpass()

	code = db.authenticate(username, password)
	if (code == 1):
		clear_screen()
		print("Invalid username or password")
	elif (code == 0):
		clear_screen()
		app.run()
		break


db.disconnect()
