import random

print ("This is a 2 player Dice game")

num1 = int(input("Player 1 Enter a number between 1 and 6: "))
num2 = int(input("Player 2 Enter a number between 1 and 6: "))

score1 = 0
score2 = 0

if num1>6:
	print ("Not a valid input Player 1")
elif num1<=0:
	print ("Not a valid input Player 1")
else:
	for x in range(6):
		game1 = random.randint(1,6)

	print ("The Player 1 dice returned: " + str(game1))

		
	if game1 == num1:
		print ("Player 1 You Won!")
		score1 = score1 + 1
	else:
		print ("Player 1 Sorry You Lost!")  

if num2>6:
	print ("Not a valid input Player 2")
elif num2<=0:
	print ("Not a valid input Player 2")
else:
	for x in range(6):
		game2 = random.randint(1,6)

	print ("The Player 2 dice returned: " + str(game2))

		
	if game2 == num2:
		print ("Player 2 You Won!")
		score2 = score2 + 1
	else:
		print ("Player 2 Sorry You Lost!")  

if score1>score2:
	print ("Player 1 Wins!")
elif score2>score1:
	print ("Player 2 Wins!")
else:
	print ("It is a Tie!")
