import mysql.connector
import os, time
import App
from Database import Database
from mysql.connector import errorcode
from getpass import getpass

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("-----Timesheet Tracker-----")

def login():
	# Connect to database
	db = Database.DB()
	dbcode = db.connect()
	if (dbcode == 0):
		cursor = db.cnx.cursor()

	while (True):
		print("Username: ", end = " ")
		username = str(input())
		password = getpass()

		code = db.authenticate(username, password)
		if (code == 1):
			print("Invalid username or password, ty again? (y/n): ", end="")
			cont = str(input())
			clear_screen()
			if (cont != "y"):
				break
		elif (code == 0):
			clear_screen()
			app = App.Timesheet(username)
			app.run()
			del app
			break
	db.disconnect()


def register():
	clear_screen()
	print("Register new user")
	print("Enter username: ", end="")
	new_user = str(input())


def main():
	clear_screen()

	while (True):
		print("1) Login")
		print("2) Register")
		print("3) Quit")
		print("Enter your option: ", end="")
		option = str(input())

		if (option == "1"):
			login()
		elif (option == "2"):
			register()
		else:
			clear_screen()
			print("Exiting timesheet tracker, goodbye.")
			time.sleep(3)
			break

	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
