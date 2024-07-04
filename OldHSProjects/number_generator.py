#This program will prompt the user to guess a number between 1 and 10. The number is pre-determined to be 3
#The while True loops make sure that the question is asked againg if the answer is wrong
#The user's guess is set to the guess variable, which is then compared to the answer variable
#If the variables match, the program stops
while True:
  while True:
    answer = int(3)
    guess = int(input('Guess a number between 1 and 10 '))
    if int(guess) == int(answer):
      print('Yes! 3 was the right answer!')
      quit()