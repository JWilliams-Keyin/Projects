# Description: Program to calculate the cost of gym 
#              memberships
# Author:      Jack Williams
# Date:        May 6, 2024
# Note that any blank print statements are meant to add a
# blank line in the ouput

# Program Constants #

FIRST_MEM_RATE = 125.00
ADD_MEM_RATE = 75.00
HST_RATE = 0.15
CANCEL_RATE = 0.60

# User Input Values #

MemNum = input('Enter the membership number: ')
print()
MemName = input(' Enter member name: ')
StAdd = input('Enter the street address: ')
PhoneNum = input('Enter the phone number: ')

# Conversion of NumFamMem from string to integer 
# consolidated into one line of code
NumFamMem = int(input('Enter the number of family members: '))
print()

# Calculations #

FirstCost = FIRST_MEM_RATE
AddCost = (NumFamMem - 1) * ADD_MEM_RATE
MemCost = FirstCost + AddCost
print()
HST = MemCost * HST_RATE
TotMemCost = MemCost + HST
print()
CancelFee = (MemCost * 3) * CANCEL_RATE

# Print Statements, Output Values To User #

print('Member number: ', MemNum)
print('Member name: ', MemName)
print('Street address', StAdd)
print('Phone number: ', PhoneNum)
print()
print('Membership Cost: $', MemCost)
print()
print('Taxes: $', HST)
print('Total Membership Cost: $', TotMemCost)
print()
print('Cancellation Fee: $', CancelFee)
