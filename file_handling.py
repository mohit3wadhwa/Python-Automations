# with open("python.txt", "w") as data_obj:
# 	name = ""
# 	while name != "quit":
# 		name = input("enter your name, or mention 'quit' to quit ")
# 		if (name == "quit"):
# 			break
# 		else:
# 			data_obj.write(name + "\n")


print("welcome to Calc\n")

while True:
	try:
		num1 = int(input("Enter First Number"))
		num2 = int(input("Enter Second Number"))

	except ValueError:
		print("Please enter Numbers instead of any character, try entering again")
		#continue
	else:
		sum = num1 + num2
		print("Sum of " + str(num1) + " and " + str(num2) + " is: " + str(sum))



