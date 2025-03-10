#This program is a simple CAD to USD money converter
#The CAD variable prompts the user to enter how much money they have
CAD = float(input('How much Canadian money do you have? $ '))
#The USD variable calculates how much money the user has in american dollars
USD = float(CAD) * float(0.79)
#The total variable rounds the answer to two decimal points
total= round(float(USD),2)
#The print function shows the user how much money they have
print('You have $', total, 'American dollars.')