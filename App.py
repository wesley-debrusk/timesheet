


class Timesheet:
	def __init__(self, user):
		self.user = user;

	def run(self):
		print("Enter a command or type 'help' for a list of commands")

		while (True):
			print(">> ", end=" ")
			command = str(input())
			if (command == "help"):
				print("help me")
			elif (command == "logout"):
				break
