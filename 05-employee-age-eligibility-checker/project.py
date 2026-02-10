def check_age(age):

	if age > 18:
		return "Congratulation! you are eligible."

	elif age == 18:
		return "Congratulation! you are qualified."

	else:
		return "Sorry! Minimum age required of 18."

name = input("Enter your name: ")
print(f"Hello {name} 👋")


while True:
	try:
		age = int(input("Enter your age: "))
		break
	except ValueError:
		print("Please enter age in number only.")

check = check_age(age)
print(check)
print("Thanks for input 😊")


