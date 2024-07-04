#This program will record 4 grades that the user inputs and calculate the overall average
#The following lines of code prompt the user to input their four grades and apply those answers to the num variables
num1 = float(input('What is your math grade? '))
num2 = float(input('What is your science grade? '))
num3 = float(input('What is your french grade? '))
num4 = float(input('What is your english grade? '))
#This code gives the weight of each subject in order to calculate appropriately
weight1 = float(num1) * float(0.2)
weight2 = float(num2) * float(0.26)
weight3 = float(num3) * float(0.14)
weight4 = float(num4) * float(0.4)
#The average variable adds all of the weight variables together and the print function shows the average
average = float(weight1) + float(weight2) + float(weight3) + float(weight4)
print('Your overall average is', average)