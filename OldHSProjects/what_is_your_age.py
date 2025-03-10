#This program determines the users age by calculating the difference between the current year and their birth year.
#These lines prompt the user to input their birth year and the current year to calculate the difference later. Those answers are then set to the current_year and birth_year variables
current_year = input('What is the current year? ')
birth_year = input('What year were you born? ')
#The age variable calculates the user's age and the print function shows the user the answer
age = int(current_year) - int(birth_year)
print('Your age is', age)