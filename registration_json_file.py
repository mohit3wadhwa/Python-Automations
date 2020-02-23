import json


def check_db():
	try:
		with open("user.json") as user_obj:
			usr_name = json.load(user_obj)
			#usr_name = user_obj.read()
			return usr_name
	except FileNotFoundError:
		usr_name = ""
		return usr_name
		

def store_user():
	user_name = input("Please Enter your name")
	
	try:
		with open("user.json", "w") as user_obj:
			json.dump(user_name,user_obj)
			#user_obj.write(user_name)
	except FileNotFoundError:
		print("hmm....Something went wrong")

	print("Thanks " + user_name + "! Will remember your name next time.")


def greet_user():
	user_name = check_db()
	if user_name:
		flag = input("Is " + user_name + " your name? - yes/no")
		if flag == 'yes':
			print("Welcome back, " + user_name)
		else:
			print("oh! ok...sorry.")
			store_user()
	else:
		store_user()
		
greet_user()
