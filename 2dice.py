import random

print ("This is a 2 Dice game")
num = int(input("Predict Total of 2 Dice Rolls: "))

if num>12:
	print ("Not a valid input")
elif num<=0:
	print ("Not a valid input")
else:
	for x in range(6):
		game1 = random.randint(1,6)

	for y in range(6):
		game2 = random.randint(1,6)
			
	total = int(game1 + game2)
	print ("Total of Two Dice Rolls is: " + str(total))

	if total == num:
		print ("You Won!")
	else:
		print ("Sorry You Lost!")  

