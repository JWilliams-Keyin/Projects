#This program will record 4 grades that the user inputs and calculate the overall average
#The following lines of code prompt the user to input their four grades and apply those answers to the num variables
num1 = float(input('What is your math grade? '))
num2 = float(input('What is your science grade? '))
num3 = float(input('What is your french grade? '))
num4 = float(input('What is your english grade? '))
#The sum variable adds all of the users grades together, then the average variable divides the sum
sum = float(num1) + float(num2) + float(num3) + float(num4)
average = float(sum) / int(4)
print('Your overall average is', average)