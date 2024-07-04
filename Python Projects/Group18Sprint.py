# Description: This program is a menu that contains all of the programs the we made
# Dates:       June 17th - June 24th, 2024
# Author:      Jack Williams

# Libraries #

import datetime
import random
import re

# Functions #

# Extra functions can be found in programs 1, 2, and 5

def Program1():
    # Author: Frank Holdbrook
    # Date:   June 18th, 2024

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
        locationofTrip=input("Enter the location of the trip : ")
        
        
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
        print()  
        
        
    #Repeat program until user terminates 
    while True:
        main()
        if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
            print("Program Terminated!!!!")
            break 


def Program2():
    # Author: Frank Holdbrook
    # Date: June 23rd, 2024
    def fizz_bizz():
    
        # To solve the FizzBizz problem with the additional "Bizz" condition for
        # numbers divisible by 8
        
        # loop shows from 1 to 100 inclusive
        for i in range(1, 101): 
        
            # if number is divisible by both 5 and 8. If true, print "FizzBizz"    

            if i % 5 == 0 and i % 8 == 0 :  
                
                print("FizzBizz") 

                #if the number is divisible by 5. If true, print "Fizz"
            elif i % 5 == 0: 
                
                print("Fizz")

                # if the number is divisible by 8. If true, print "Bizz"
            elif i % 8 == 0: 
                print("Bizz")
            else:
                
                # If none of the above conditions are true, print the number itself          
                print(i) 

    fizz_bizz()
    print()


def Program3():
    #Zackery Strickland
    #Date: Tue, June, 18
    #Midterm Sprint #1.


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
    print()


def Program4():
    # Description: This program generates maintinence schedules for the XYZ Company.
    #              It takes the user inputted price of equipment and purchase date,
    #              then gives the user a maintinence schedule for the equipment.
    # Author:      Jack Williams
    # Date:        June 17th, 2024

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

    while True:
        EquipCost = input('Enter the cost of the equipment: ')
        print()
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


def Program5():
    #Zackery Strickland
    #Date: Tue, June, 21
    #Midterm Sprint #1.
    #Decided to Make minesweeper as it would have need and old stuff for me to research

    # lets create a board object to represent the minesweeper game
    # this is so that we can just say "create a new board object", or
    # "dig here", or "render this game for this object"
    class Board:
        def __init__(self, dim_size, num_bombs):
        
            self.dim_size = dim_size
            self.num_bombs = num_bombs

            # let's create the board
            
            self.board = self.make_new_board() # plant the bombs
            self.assign_values_to_board()

            # initialize a set to keep track of which locations we've uncovered
            # we'll save (row,col) tuples into this set 
            self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

        def make_new_board(self):
            # construct a new board based on the dim size and num bombs
            # we should construct the list of lists here (or whatever representation you prefer,
            # but since we have a 2-D board, list of lists is most natural)

            # generate a new board
            board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
            # this creates an array like this:
            # [[None, None, ..., None],
            #  [None, None, ..., None],
            #  [...                  ],
            #  [None, None, ..., None]]
            # we can see how this represents a board!


            # plant the bombs
            bombs_planted = 0
            while bombs_planted < self.num_bombs:
                loc = random.randint(0, self.dim_size**2 - 1) # return a random integer N such that a <= N <= b
                row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us what row to look at
                col = loc % self.dim_size  # we want the remainder to tell us what index in that row to look at

                if board[row][col] == '*':
                    # this means we've actually planted a bomb there already so keep going
                    continue

                board[row][col] = '*' # plant the bomb
                bombs_planted += 1

            return board

        def assign_values_to_board(self):
            # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
            # represents how many neighboring bombs there are. we can precompute these and it'll save us some
            # effort checking what's around the board later on :)
            for r in range(self.dim_size):
                for c in range(self.dim_size):
                    if self.board[r][c] == '*':
                        # if this is already a bomb, we don't want to calculate anything
                        continue
                    self.board[r][c] = self.get_num_neighboring_bombs(r, c)

        def get_num_neighboring_bombs(self, row, col):
            # let's iterate through each of the neighboring positions and sum number of bombs
            # top left: (row-1, col-1)
            # top middle: (row-1, col)
            # top right: (row-1, col+1)
            # left: (row, col-1)
            # right: (row, col+1)
            # bottom left: (row+1, col-1)
            # bottom middle: (row+1, col)
            # bottom right: (row+1, col+1)

            # We need to make sure to not go out of bounds

            num_neighboring_bombs = 0
            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if r == row and c == col:
                        # our original location, don't check
                        continue
                    if self.board[r][c] == '*':
                        num_neighboring_bombs += 1

            return num_neighboring_bombs

        def dig(self, row, col):
            # dig at that location!
            # return True if successful dig, False if bomb dug

            # a few scenarios:
            # hit a bomb -> game over
            # dig at location with neighboring bombs -> finish dig
            # dig at location with no neighboring bombs -> recursively dig neighbors!

            self.dug.add((row, col)) # keep track that we dug here

            if self.board[row][col] == '*':
                return False
            elif self.board[row][col] > 0:
                return True

            # self.board[row][col] == 0
            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if (r, c) in self.dug:
                        continue # don't dig where you've already dug
                    self.dig(r, c)

            # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
            return True
            # self.board[row][col] == 0
            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if (r, c) in self.dug:
                        continue # don't dig where you've already dug
                    self.dig(r, c)

            # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
            return True

        def __str__(self):
            # this is a magic function where if you call print on this object,
            # it'll print out what this function returns
            # return a string that shows the board to the player

            # first let's create a new array that represents what the user would see
            visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
            for row in range(self.dim_size):
                for col in range(self.dim_size):
                    if (row,col) in self.dug:
                        visible_board[row][col] = str(self.board[row][col])
                    else:
                        visible_board[row][col] = ' '
            
            # put this together in a string
            string_rep = ''
            # get max column widths for printing
            widths = []
            for idx in range(self.dim_size):
                columns = map(lambda x: x[idx], visible_board)
                widths.append(
                    len(
                        max(columns, key = len)
                    )
                )

            # print the csv strings
            indices = [i for i in range(self.dim_size)]
            indices_row = '   '
            cells = []
            for idx, col in enumerate(indices):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            indices_row += '  '.join(cells)
            indices_row += '  \n'
            
            for i in range(len(visible_board)):
                row = visible_board[i]
                string_rep += f'{i} |'
                cells = []
                for idx, col in enumerate(row):
                    format = '%-' + str(widths[idx]) + "s"
                    cells.append(format % (col))
                string_rep += ' |'.join(cells)
                string_rep += ' |\n'

            str_len = int(len(string_rep) / self.dim_size)
            string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

            return string_rep

    # play the game
    def play(dim_size=10, num_bombs=10):
        # Step 1: create the board and plant the bombs
        board = Board(dim_size, num_bombs)

        # Step 2: show the user the board and ask for where they want to dig
        # Step 3a: if location is a bomb, show game over message
        # Step 3b: if location is not a bomb, dig recursively until each square is at least
        #          next to a bomb
        # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
        safe = True 

        while len(board.dug) < board.dim_size ** 2 - num_bombs:
            print(board)
            # 0,0 or 0, 0 or 0,    0
            user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
            row, col = int(user_input[0]), int(user_input[-1])
            if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                print("Invalid location. Try again.")
                continue

            # if it's valid, we dig
            safe = board.dig(row, col)
            if not safe:
                
                break 

        # 2 ways to end loop, lets check which one
        if safe:
            print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
        else:
            print("SORRY GAME OVER :(")
            
            board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
            print(board)

    if __name__ == '__main__': 
        play()


# Input Statements #

while True:
    print('Midterm Sprint - Main Menu')
    print()
    print('1. Complete a travel claim.')
    print('2. Fun Interview Question.')
    print('3. Cool stuff with strings and dates.')
    print('4. A little bit of everything.')
    print('5. Something old, something new.')
    print('6. Quit.')
    print()
    
    while True:
        Choice = input('Enter choice (1-6): ')
        print()
        if Choice == '1':
            Program1()
            break
        elif Choice == '2':
            Program2()
            break
        elif Choice == '3':
            Program3()
            break
        elif Choice == '4':
            Program4()
            break
        elif Choice == '5':
            Program5()
            break
        elif Choice == '6':
            exit()
        else:
            print('ERROR: Invalid option entered. Please enter 1, 2, 3, 4, 5, or 6 only.')
            print()