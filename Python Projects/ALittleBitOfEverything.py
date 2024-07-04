# Description: This program generates maintinence schedules for the XYZ Company.
#              It takes the user inputted price of equipment and purchase date,
#              then gives the user a maintinence schedule for the equipment.
# Author:      Jack Williams
# Date:        June 17th, 2024

# Libraries #

import datetime

# Constants #

SALVAGE_RATE = 0.10
AMORT_RATE = 180.0

# Input Statements #

print()
print('XYZ Company')
print('Equipment Maintenence')
print()
print('Please give all prompted information')
print()

EquipCost = input('Enter the cost of the equipment: ')
print()
while True:
    if EquipCost == '':
        print('ERROR: The cost of the equipment must be entered')
        print()
        EquipCost = input('Enter the cost of the equipment: ')
        print()
    elif EquipCost.isalpha() == True or EquipCost.isspace() == True:
        print('ERROR: The equipment cost you entered is invalid')
        print('NOTE: Enter only the numeric value, do not add any spaces or extra characters other than a decimal')
        print()
        EquipCost = input('Enter the cost of the equipment: ')
        print()
    else:
        EquipCost = float(EquipCost)
        break


while True:
    try:
        PurchDate = input('Enter the date the equipment was purchased (YYYY-MM-DD): ')
        PurchDate = datetime.datetime.strptime(PurchDate, '%Y-%m-%d')
    except:
        print('ERROR: The date you entered is invalid')
    else:
        break


# Calculations #

PurchDay = PurchDate.day
PurchMonth = PurchDate.month
PurchYear = PurchDate.year

PurchMonth += 6
if PurchMonth >= 13:
    PurchMonth -= 12
    PurchYear += 1

MajorInspec = datetime.datetime(PurchYear, PurchMonth, PurchDay)

SalvageValue = EquipCost * SALVAGE_RATE
Amortization = (EquipCost - SalvageValue) / AMORT_RATE

BasicClean = PurchDate + datetime.timedelta(days = 10)
TubeCheck = PurchDate + datetime.timedelta(weeks = 3)

EquipCostDsp = '${:,.2f}'.format(EquipCost)
SalvageValueDsp = '${:,.2f}'.format(SalvageValue)
AmortizationDsp = '${:,.2f}'.format(Amortization)

PurchDateDsp = PurchDate.strftime('%Y-%m-%d')
BasicCleanDsp = BasicClean.strftime('%Y-%m-%d')
TubeCheckDsp = TubeCheck.strftime('%Y-%m-%d')
MajorInspecDsp = MajorInspec.strftime('%Y-%m-%d')

# Display #

print()
print(f'---------------------------------------------------------------------')
print(f'                     Equipment Maintenence Schedule')
print(f'                               XYZ Company')
print()
print(f'         Equipment Information              Maintenece Dates        ')
print(f'                                    ||                                ')
print(f'Purchase Date:        {PurchDateDsp:<10s}    || Basic Cleaning:     {BasicCleanDsp:<10s}')
print(f'Price:                {EquipCostDsp:<13s} || Tube & Fluid Check: {TubeCheckDsp:<10s}')
print(f'Salvage Value:        {SalvageValueDsp:<13s} || Major Inspection:   {MajorInspecDsp:<10s}')
print(f'Monthly Amortization: {AmortizationDsp:<12s}  ||                                             ')
print(f'---------------------------------------------------------------------')
print()