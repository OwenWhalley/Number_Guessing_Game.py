from random import *
a = randint(1, 6)

guess = int(input("Select a number between 1 and 6:"))
if a == guess:
  print("You guessed right!")
else:
  print("The answer is: %d" %(a))