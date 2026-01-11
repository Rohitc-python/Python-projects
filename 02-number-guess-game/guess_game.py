"""
Number Guess Game
Author: Rohit Chaudhary
Discription: A simple python game where user guesses  a random number
"""
import random  # random module to generate random number

# generate a  random number between 1 and 100
secret_number = random.randint(1,100)

guess = None       # store user's guess
attemts = 0        # conunt number of attemps

print("Number Guess Game.")
print("I have thought of a number between 1 and 100")

# Loop will run until user guesses the correct number
while guess !=secret_number:
	guess = int(input("Write your guess number:"))
	attemts += 1

	if guess > secret_number:
		print("NO buddy , your number is High.")
	elif guess < secret_number:
		print("NO buddy, your number is Low.")
	else:
		print("Congrats buddy, you'r Right.")
		print(f"you guessed it in  {attemts} attemps.")





