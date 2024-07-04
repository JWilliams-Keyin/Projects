import datetime

def main():

    RENTRATE = 65.00
    BONUS = 0.0
    
#employeeNumber
    while True:
        try:
            employeeNumber = input("What is your employee number ? ")
            if (employeeNumber == "QUIT"):
                print("Program Terminatted !!!")
                quit()
            elif len(employeeNumber) != 5:
                print("Employee number is required and must be 5 characters")
            else:
                break
        except Exception as e:
            break
        
        
    # employeefirstname
    while True:
        try:
            employeefirstname = (input("What is your first name ? ")).title()
            if employeefirstname == "" :
                print("First Name is required")
            else:
                break
        except Exception as e:
            break  
    
    
    # employeelastname
    while True:
        try:
            employeelastname = (input("What is your last name ? ")).title()
            if employeelastname == "" :
                print("Last Name is required")
            else:
                break
        except Exception as e:
            break  
    
    #Trip location
    locationofTrip=input("Enter the loaction of the trip : ")
    
    
    #Date
    
    while True:
                try:
                    start_date = datetime.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
                    end_date = datetime.datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
                    if start_date > end_date:
                        print("Start date cannot be after end date. Please re-enter.")
                        continue
                    elif (end_date - start_date).days > 7:
                        print("Trip duration cannot exceed 7 days. Please re-enter.")
                        continue
                    break
                except ValueError:
                    print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
    
    #Car Type
    while True:
                car_type = input("Car used (O for own, R for rented): ").strip().upper()
                if car_type not in ['O', 'R']:
                    print("Invalid input. Enter O or R.")
                else:
                    break
    
    # Kilometers validation
    kilometers = 1
    if car_type == 'O':
                while True:
                    try:
                        kilometers = float(input("Total kilometers traveled (up to 2000 km): "))
                        if kilometers <= 0 or kilometers > 2000:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Kilometers must be a number between 0 and 2000.")
        
    
    #Claim Type
    while True:
                claimType = input("Claim type (S for standard, E for executive): ").strip().upper()
                if claimType not in ['S', 'E']:
                    print("Invalid input. Enter S or E.")
                else:
                    break
    
    
    days = (end_date - start_date).days
    
    
    #perdiem
    perDiem = days * 85.00
    mileageAmount = 0.17 * kilometers if ( car_type == "O" ) else RENTRATE * days
    
    
    if days > 3:
        BONUS += 100.00
    
    if car_type == "O" and kilometers > 1000:
        BONUS += 0.04 * kilometers
    
    if claimType == "E" :
        BONUS += 45.00    
    
    if datetime.datetime(start_date.year, 12, 15) <= start_date <= datetime.datetime(start_date.year, 12, 22):
            BONUS += days * 50.00
    
    #Claim Amount
    claimAmount = perDiem + mileageAmount + BONUS
    #Taxes
    HST = claimAmount * 0.15
    #Claim Total
    claimTotal = HST + claimAmount
    
    #Output Results

    print("------------------------------------ NL CHOCOLATE COMPANY ---------------------------------------------")    
    print("-------------------------------------------------------------------------------------------------------")    
    print("------------------------------------ EMPLOYEE TRAVEL CLAIM --------------------------------------------")    
    print(employeefirstname + " " + employeelastname + " " + employeeNumber + "--------------------------------------------------------------------------")    
    print(locationofTrip + " - " + str(start_date) + " to " + str(end_date) + "------------------------------------------------------")    
    print(car_type + " - " + str(kilometers) + " kilometers " + " - Claim Type " + claimType + "-" + "$" + str(claimAmount) + "------------------------------------------------------------------")    
    print("-------------------------------------------------------------------------------------------------------")    
    print("-------------------------------------------------------------------------------------------------------")    
    print("Mileage amount is " + str(mileageAmount) + "-------------------------------------------------------------------------------")
    print("PerDiem is " + str(perDiem) + "-----------------------------------------------------------------------------------------------")
    print("BONUS is " + str(BONUS) + "------------------------------------------------------------------------------------------------")
    print("HST is " + str(HST) + "----------------------------------------------------------------------------------------------------")
    print("Claim Total is " + str(claimTotal) + "-------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------")    
    print("-------------------------------------------------------------------------------------------------------")    
    
    
 #Repeat program until user terminates 
while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        print("Program Terminated!!!!")
        break 