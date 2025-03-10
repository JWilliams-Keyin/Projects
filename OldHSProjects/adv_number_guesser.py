#This program prompts the user to guess a number between 1 and 10 that is randomly generated
#The randint function picks a random number between the range that is inputted
#The incorrect variable determines if the guess is incorrect by setting the loop to false if the user guesses the answer
from random import randint
answer = randint(1, 10)
guess = int(input('Guess a number between 1 and 10 '))
incorrect = True
while True:
  if guess == answer:
    incorrect = False
    print('Yes! the answer was', answer)
    quit()
  elif guess != answer:
    guess = int(input('Guess a number between 1 and 10 '))