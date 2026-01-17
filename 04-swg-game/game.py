import random

print("Choose: Gun(0), Water(1), Snake(2)")


while True:
	choose = random.randint(0,2)
	user = int(input("Enter your choice: "))
	
	if choose==user:
		print("👑Draw match")
	elif (
		(choose==0 and user==2) or 
		(choose==2 and user==1) or
		(choose==1 and user==0) 
		):
		print("👑Computer Winner")
	
	else:
		print("👑You Winner")


	print(f"Computer choose: {choose}")

	again = input("Play again? (y/n): ")
	if again.lower() != 'y':
		break
    	

