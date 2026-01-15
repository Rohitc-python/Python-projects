print("*" * 30)
print("Hii guys! I am Rohit.")
print("Today i'll normal conversation to you, okay.")
print("-" * 30)

choose = input("Do you want to talk to me? (yes/no): ").lower()

if choose == "yes":
	print("Nice choice 👍")
	name = input("Enter your name: ")
	age = int(input("Enter your age: "))
	if age < 18:
		print(f"Hey {name}, you're {age} year old ")
	elif age == 18:
		print(f"Hey {name}, you're {age} year old")
	else:
		print(f"Hey {name}, you're {age} year old , {name}")
else:
	print(f"okay ,your coice. ")





