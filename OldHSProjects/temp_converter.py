#This program converts temperature from C to F or F to C
#The user is prompted to input the tempurature and measurement. The temp and sign variables are set to their answers
temp = int(input('What is the temperature? '))
sign = input('Choose C or F ')
#This loop calculates the conversion from C ro F or F to C. If neither are inputted, an error is given and the program stops
if sign.upper() == 'C':
  result = int((9*temp)/5 + 32)
  sign_output = 'farenheit'
elif sign.upper() == 'F':
  result = int((temp - 32)* 5 / 9)
  sign_output = 'celcius'
else:
  print('You must input either C or F')
  quit()
#This string shows the converted tempurature
print('The tempurature in', sign_output, 'is', result, 'degrees')