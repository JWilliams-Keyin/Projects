# Testing grounds for the date variable examples in my python notes #
# Remove and add comments to programs to test each #

import datetime

CUR_DATE = datetime.datetime.now()

# Adding and subtracting days #

CurYear = CUR_DATE.year
CurMonth = CUR_DATE.month
CurDay = CUR_DATE.day 

CurYear += 3

NewDate = datetime.datetime(CurYear, CurMonth, CurDay)
print(NewDate)


# Travel claim example #
'''''''''
while True:
    try:
        StartDate = input('Enter the start date (YYYY-MM-DD): ')
        StartDate = datetime.datetime.strptime(StartDate, '%Y-%m-%d')
    except:
        print('   Data Entry Error - start date is not a valid format')
    else:
        break

while True:
    try:
        EndDate = input('Enter the end date (YYYY-MM-DD): ')
        EndDate = datetime.datetime.strptime(EndDate, '%Y-%m-%d')
    except:
        print('   Data Entry Error - end date is not a valid format.')
    else:
        if EndDate < StartDate:
            print('   Data Entry Error - end date must be later than the start date.')
        else:
            break

NumDays = (EndDate - StartDate).days
if NumDays == 0:
    NumDays = 1
TotalClaim = NumDays * 56.00 # The 56 dollars would be a constant in actual programs, as it is a per diem rate which can be changed in the future #

print(NumDays)
print(TotalClaim)
'''''''''