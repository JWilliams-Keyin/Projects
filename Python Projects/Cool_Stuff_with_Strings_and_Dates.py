#Zackery Strickland
#Date: Tue, June, 18
#Midterm Sprint #1.

#inports
import datetime

#Input
while True:
    EmpFirstName = input("Please enter employee first name: ").title()
    if not EmpFirstName:
        print("Error something must be entered")
    else:
        break

while True:
    EmpLastName = input("Please enter employee last name: ")
    if not EmpLastName:
        print("Error something must be entered")
    else:
        break

while True:
    EmpPhoneNum = input("Please enter employee's 10-digit phone number(##########): ")
    if not EmpPhoneNum:
        print("Error something must be entered")
    elif not EmpPhoneNum.isdigit():
        print("Error only numbers may be entered")
    elif len(EmpPhoneNum) !=10:
        print("Error phone number has to be 10 digets")
    else:
        break

while True:
    CurrentDate = input("Please enter the current date (YYYY-MM-DD): ")
    if not CurrentDate:
        print("Error something must be entered")
    else:
        try:
            CurrentDateDO = datetime.datetime.strptime(CurrentDate, "%Y-%m-%d")
        except:
            print("Error must follow year, month, day format")
        else:
            break

while True:
    EmpStartDate = input("Please enter the employee start date (YYYY-MM-DD): ")
    if not EmpStartDate:
        print("Error something must be entered")
    else:
        try:
            EmpStartDateDO = datetime.datetime.strptime(EmpStartDate, "%Y-%m-%d")
        except:
            print("Error must follow year, month, day format")
            
        else:
             break

while True:
    EmpBirthday = input("Please enter employee birthday (YYYY-MM-DD): ")
    if not EmpBirthday:
        print("Error something must be entered")
    else:
        try:
            EmpBirthdayDO = datetime.datetime.strptime(EmpBirthday, "%Y-%m-%d")
        except:
            print("Error must follow year, month, day format")
        else:
            break

EmpId = EmpStartDate[0:4]+EmpStartDate[5:7]+EmpStartDate[8:]+ EmpBirthday[0:4]+EmpBirthday[5:7]+EmpBirthday[8:]

Username = EmpFirstName[0]+EmpLastName[0]+EmpPhoneNum[6:]

TimeWorked = (CurrentDateDO - EmpStartDateDO).days

ThisYearsBirthday = datetime.datetime(CurrentDateDO.year, EmpBirthdayDO.month, EmpBirthdayDO.day)

if ThisYearsBirthday<CurrentDateDO:

    NextBirthday = datetime.datetime(CurrentDateDO.year +1, EmpBirthdayDO.month, EmpBirthdayDO.day)
else:
    NextBirthday = ThisYearsBirthday

DaysTillBirthday = (NextBirthday - CurrentDateDO).days

RetiredDate = datetime.datetime(EmpBirthdayDO.year +65, EmpBirthdayDO.month, EmpBirthdayDO.day)

DaysTillRetired = (RetiredDate - CurrentDateDO).days

print(f"Employee ID:        ${EmpId}")
print(f"Username:           ${Username}")
print(f"Time Worked:        ${TimeWorked}")
print(f"Days Till Birthday: ${DaysTillBirthday}")
print(f"Days Till Retired:  ${DaysTillRetired}")


