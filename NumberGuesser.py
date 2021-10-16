# This a Random Number Guesser I made back in my early days of Python, I see it asked of beginners 
# to test their skills, so I wanted to put it up for a reference

import random

# This function allows users to try and guess a randomly generated number
def func1():
	x = random.randint(1, 100)
	# CPU always goes first and will always guess the hafl point of the range to narrow down results
	counter = 0

	print("Please guess a number between 0 and 100: ")
	
	while(True):
		counter += 1
		guess = int(input())
		if guess == x:
			if counter == 1:
				print("Congrats! You guessed correct in 1 try! The answer was " + str(guess) + "!\n")
				break
			else: 
				counter = str(counter)
				print("Congrats! You guessed correct in " + counter + " tries! The answer was " + str(guess) + "!\n")
				break
		elif guess < x:
			print("Your guess is too low.")
		elif guess > x:
			print("Your guess is too high.")

# This function allows users to watch a CPU guess, using a similar algorithm to a binary search that I thought up
def func2():
	x = random.randint(1, 100)
	# Gives us our counter for the amount of guesses it took
	counter = 0
	# CPU always goes first and will always guess the hafl point of the range to narrow down results
	guess = 50
	# The adder increments the new guess of the CPU by half of the previous guess, by subtraction or addition as needed
	adder = 50
	# Stores guesses in a list so that CPU doesn't get stuck in a loop or makes the same guess twice
	guessList = []

	while True:
		counter += 1
		guessList.append(guess)
		if guess == x:
			print(guess)
			counter = str(counter)
			print("Congrats! The CPU guessed correct in " + counter + " tries! The answer was " + str(guess) + "!\n")
			break
		elif guess < x:
			print(guess)
			print("Your guess is too low.")
			adder = int(.5 * adder)
			if adder == 0:
				adder = 2
			guess = guess + adder
			if guess in guessList:
				guess += 1
		elif guess > x:
			print(guess)
			print("Your guess is too high.")
			adder = int(.5 * adder)
			if adder == 0:
				adder = 2
			guess = guess - adder  
			if guess in guessList:
				guess -= 1

def func3():
	x = random.randint(1, 100)
	# Gives us our counter for the amount of guesses it took the User
	counter = 0
	# Gives us our counter for the amount of guesses it took the CPU
	counterCPU = 0
	# Allows program to dictate whos turn it is
	turn = 0
	# CPU always goes first and will always guess the hafl point of the range to narrow down results
	guess = 50
	# The adder increments the new guess of the CPU by half of the previous guess, by subtraction or addition as needed
	adder = 50
	# Stores guesses in a list so that CPU doesn't get stuck in a loop or makes the same guess twice
	guessList = []

	print("Please guess a number between 0 and 100: ")

	while True:
		turn += 1
		if turn % 2 == 0:
			guess2 = int(input("\nUser's Turn: "))
			guessList.append(guess2)
			counterCPU += 1
			if guess2 == x:
				if counterCPU == 1:
					print("Congrats! You guessed correct in 1 try!")
					break
				else: 
					counterCPU = str(counterCPU)
					print("Congrats! You guessed correct in " + counterCPU + " tries!")
					break
			elif guess2 < x:
				print("Your guess is too low.")
			elif guess2 > x:
				print("Your guess is too high.")
		else:
			counter += 1
			if guess in guessList and guess != 100:
				guess += 1
			elif guess in guessList and guess == 100:
				guess -= 1
			guessList.append(guess)
			if guess == x:
				print("\nCPU's Turn: " + str(guess))
				counter = str(counter)
				print("The CPU guessed correct in " + counter + " tries! You Lose!")
				break
			elif guess < x:
				print("\nCPU's Turn: " + str(guess))
				print("Your guess is too low.")
				adder = int(.5 * adder)
				if adder == 0:
					adder = 2
				guess = guess + adder
				if guess in guessList:
					guess += 1
			elif guess > x:
				print("\nCPU's Turn: " + str(guess))
				print("Your guess is too high.")
				adder = int(.5 * adder)
				if adder == 0:
					adder = 2
				guess = guess - adder
				if guess in guessList:
					guess -= 1



# This will serve as our "Main" function
def main():
	while(True):
		print("Game Modes:")
		print("1. User Guessing")
		print("2. CPU Guessing")
		print("3. User vs CPU")
		print("Select any other character to exit")
		gameMode = int(input("Please select 1, 2, or 3: "))

		if gameMode == 1:
			func1()
		elif gameMode == 2:
			func2()
		elif gameMode == 3:
			func3()
		else:
			print("Thanks for playing!")
			break

main()