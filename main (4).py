from random import *

#Assign a random number between 1 and 6 to the variable a.
a = randint(1, 6)

#Ask for a number between 1 and 6 and assign it to the variable guess.
guess = int(input("Select a number between 1 and 6:"))

#Using an if else statement to tell the user whether a = guess, or does not equal guess along with the value of a.
if a == guess:
  print("You guessed right!")
else:
  print("The answer is: %d" %(a))