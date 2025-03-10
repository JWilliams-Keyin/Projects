# Description: This program is used to calculate travel 
#              claims
# Author:      Jack Williams
# Dates:       May 1, 2024 - 

# Program Constants #

PER_DIEM_RATE = 56.00
LODGING_RATE = 125.00
MIL_RATE = 0.24
HST_RATE = 0.15

# User Input Values #

SalesName = input('Enter the salesperson name: ')
TripLoc = input('Enter the trip location: ')

# Conversion of NumDays and NumKms values from strings
# to integers consolidated into one line of code each
NumDays = int(input('Enter the number of days: '))
NumKms = int(input('Enter the number of kilometers: '))

# Calculations #

PerDiemAmt = NumDays * PER_DIEM_RATE
NumNights = NumDays - 1
LodgingAmt = NumNights * LODGING_RATE
MilAmt = NumKms * MIL_RATE
TotClaim = PerDiemAmt + LodgingAmt + MilAmt
HST = (PerDiemAmt + LodgingAmt) * HST_RATE
ClaimTotal = TotClaim + HST

# Print Statements, Output for Calculations #

print('Salesperson name: ', SalesName)
print('Trip Location: ', TripLoc)
print('Number of days: ', NumDays)
print('Number of kilometers travelled: ', NumKms, 'km')
print('Per Diem Amount: $', PerDiemAmt)
print('Lodging Amount: $', LodgingAmt)
print('Mileage Amount: $', MilAmt)
print('Total Claim: $', TotClaim)
print('Taxes (HST): $', HST)
print('Claim Total: $', ClaimTotal)