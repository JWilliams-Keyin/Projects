# Description: This program is an invoice calculator for a car rental company
# Author:      Jack Williams
# Dates:       May 8th, 2024 - May 13th, 2024

# Note: I decided to format my input values and print statements for extra practice

# Program Constants #

RENT_RATE = 55.00
KM_RATE = 0.24
INSUR_RATE = 14.00
HST_RATE = 0.15

# User Input Values #

print(f'Edsel Car Rental')
print()
print('Please enter the following values:')
print()
UserName =     input('Name: ')
PhoneNum =     input('Phone number (+*_***_****): ')
print()
RentDays = int(input('Days rented: '))
OGOdom =   int(input('Original odometer reading (*****): '))
NewOdom =  int(input('Returned odometer reading (*****): '))

# Calculations #

KmTravel = NewOdom - OGOdom

RentCost = RentDays * RENT_RATE
MilCost = KmTravel * KM_RATE          
InsurCost = RentDays * INSUR_RATE

RentDisc = RentCost * 0.10
MilDisc = MilCost * 0.25
TotDisc = RentDisc + MilDisc

TotCost = RentCost + MilCost + InsurCost - TotDisc
HST = TotCost * HST_RATE

Invoice = TotCost + HST

# Print Statements #

print()
print(f'                                Rental Invoice')
print()
print(f'Customer name:    {UserName}')
print(f'Phone number:     {PhoneNum}')
print()
print(f'Number of days rented:     {RentDays:5d}       Rental Cost:     ${RentCost:,.2f}')
print(f'Original odometer reading: {OGOdom:5d}km     Mileage Cost:    ${MilCost:,.2f}')
print(f'Returned odometer reading: {NewOdom:5d}km     Insurance Cost:  ${InsurCost:,.2f}')
print(f'Kilometers travelled:      {KmTravel:5d}km')
print(f'                                       Winter Discount: ${TotDisc:,.2f}')
print()
print(f'                                       Total Cost:      ${TotCost:,.2f}')
print(f'                                       HST:             ${HST:,.2f}')
print()
print(f'                                       Final Invoice:   ${Invoice:,.2f}')