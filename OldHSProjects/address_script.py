#This program prompts the user for their name, address, city, and postal code to output the answer in different ways

#Below are strings of code for each question. The answers will be set to the user's answers

name = input('What is your name? ')

house = input('Where do you live? ')

city = input('What city do you live in? ')

province = input('What province do you live in? ')

code = input('What is your postal code? ')

#These strings output the variables in different formats, either uppercase, lowercase, or as a title

print(name.upper())

print(house.lower())

print((city.title()), (province.upper()))

print(code.upper())