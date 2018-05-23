import random

print ("This is a Dice game")
num = int(input("Enter a number between 1 and 6: "))

if num>6:
	print ("Not a valid input")
elif num<=0:
	print ("Not a valid input")
else:
	for x in range(6):
		game = random.randint(1,6)

	print ("The dice returned: " + str(game))

		
	if game == num:
		print ("You Won!")
	else:
		print ("Sorry You Lost!")  
