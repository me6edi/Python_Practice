class User:
	name = ''
	email = ''
	password = ''

	def login(self):
		email = input("Enter email: ")
		password = input("Enter password: ")

		if email == self.email and password == self.password:
			login = True
			print("Login Successful!")
		else:
			print("Login Faild!")

	def logout(self):
		login = False
		print("Logged Out!")

	def isloggedin(self):
		if self.login:
			return True
		else:
			return False

		# def profile(self):
		# 	if self.isloggedin():
		# 		print(self.name,"\n",self.email)
		# 	else:
		# 		print("User is not Loggd in!")


user1 = User()

user1.name = "Niamul"
user1.email = "niamulhassanbd@gmail.com"
user1.password = "12345"

user1.login()
user1.profle()

hello = input()