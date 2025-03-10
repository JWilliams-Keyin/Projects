#Allows us to manipulate time in our program

import time

#This program will add the value of 1 until it reaches 100 and stops

#The counter variable is declared at the onset of the script

counter = 0

#The while loop is a conditional loop that determines the value of the counter. When the value is greater than or equal to 100, the loop stops

while counter <= 100:
  counter = counter + 1
  print(counter)
  time.sleep(0.2)

#The time.sleep function puts a delay in between each number