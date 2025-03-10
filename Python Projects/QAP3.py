# Description: This program keeps track of sales for Honest Harry Car Sales and
#              prints reciepts for new sales
# Author:      Jack Williams
# Date:        June 6th, 2024 - June 11th, 2024

# Libraries #

import datetime

# Constants #

CUR_DATE = datetime.datetime.now()
LIC_RATE_SMALL = 75.00
LIC_RATE_BIG = 165.00
TRAN_RATE = 0.01
LUX_RATE = 0.016
HST_RATE = 0.15
FINANCE_RATE = 39.99

# Input Statements #

print()
print("Honest Harry Car Sales")
print()
print('Please fill out all fields')
print()
while True:
    FirstName = input('Enter your first name OR type END to exit the program: ')
    print()
    while True:
        if FirstName == "END":
            exit()
        elif FirstName == '':
            print('ERROR: Your first name must not be blank')
            print()
            FirstName = input('Please enter your first name: ')
            print()
        else:
            FirstName = FirstName.title()
            break


    LastName = input('Enter your last name: ').title()
    print()
    while True:
        if LastName == '':
            print('ERROR: Your last name must not be blank')
            print()
            LastName = input('Please enter your last name: ').title()
            print()
        else:
            break
    

    PhoneNum = input('Enter your phone number (XXXXXXXXXX): ')
    print()
    while True:
        if PhoneNum == '':
            print('ERROR: Your phone number must not be blank')
            print()
            PhoneNum = input('Please enter your phone number (XXXXXXXXXX): ')
            print()
        elif PhoneNum.isnumeric() == False:
            print('ERROR: Your phone number must be numerical only')
            print('NOTE: Enter just the numbers, no extra characters or spaces')
            print()
            PhoneNum = input('Please enter your phone number (XXXXXXXXXX): ')
            print()
        elif len(PhoneNum) != 10:
            print('ERROR: Your phone number must be ten digits long')
            print()
            input('Please enter your phone number (XXXXXXXXXX): ')
            print()
        else:
            break


    PlateNum = input("Enter your car's license plate number (XXX999): ").upper()
    Plate1 = PlateNum[0:3]
    Plate2 = PlateNum[3:7]
    print()
    while True:
        if PlateNum == '':
            print("ERROR: Your car's plate number must be entered")
            print()
            PlateNum = input("Enter your car's license plate number (XXX999): ").upper()
            print()
            Plate1 = PlateNum[0:3]
            Plate2 = PlateNum[3:7]
        elif len(PlateNum) != 6:
            print("ERROR: Your car's plate number must contain six characters")
            print('NOTE: The first three characters are letters, and the last three')
            print('characters are numbers. Do not add any spaces or dashes')
            print()
            PlateNum = input("Enter your car's license plate number (XXX999): ").upper()
            print()
            Plate1 = PlateNum[0:3]
            Plate2 = PlateNum[3:7]
        elif Plate1.isalpha() == False or Plate2.isnumeric() == False:
            print("ERROR: Your car's liscense plate number must be three letters followed by three numbers")
            print()
            PlateNum = input("Enter your car's license plate number (XXX999): ").upper()
            print()
            Plate1 = PlateNum[0:3]
            Plate2 = PlateNum[3:7]
        else:
            break
    

    CarMake = input("Enter the make of your car: ").title()
    print()
    while True:
        if CarMake == '':
            print('ERROR: The make of your car must be entered')
            print()
            CarMake = input("Enter the make of your car: ").title()
            print()
        else:
            break


    CarModel = input("Enter the model of your car: ").title()
    print()
    while True:
        if CarModel == '':
            print('ERROR: The model of your car must be entered')
            print()
            CarModel = input("Enter the model of your car: ").title()
            print()
        else:
            break


    CarYear = input("Enter the year your car was made: ")
    print()
    while True:
        if CarYear == '':
            print('ERROR: The year your car was made must be entered')
            print()
            CarYear = input("Enter the year your car was made: ")
            print()
        elif CarYear.isnumeric() == False:
            print('ERROR: The year you entered is invalid')
            print('NOTE: Enter the year as a numeric value (Ex: 2011)')
            print()
            CarYear = input('Enter the year your car was made: ')
            print()
        elif len(CarYear) <= 4:
            print('ERROR: The year you entered is invalid')
            print('NOTE: Enter the year as a numeric value (Ex: 2011)')
            print()
            CarYear = input('Enter the year your car was made: ')
            print()
        else:
            break
    

    SellPrice = input("Enter the sale price of your car (#####.##): ")
    print()
    while True:
        if SellPrice == '':
            print('ERROR: The sale price of your car must be entered')
            print()
            SellPrice = input('Enter the sale price of your car (#####.##): ')
            print()
        elif SellPrice.isalpha() == True or SellPrice.isspace() == True:
            print('ERROR: The sale price you entered is invalid')
            print('NOTE: Enter only the numeric value, do not add any spaces or extra characters other than a decimal')
            print()
            SellPrice = input('Enter the sale price of your car (#####.##): ')
            print()
        elif float(SellPrice) >= 50000.00:
            print('ERROR: Sale price cannot exceed $50,000.00')
            print()
            SellPrice = input('Enter the sale price of your car (#####.##): ')
            print()
        else:
            SellPrice = float(SellPrice)
            break
    
    
    TradeIn = input("Enter the trade in value of your car (#####.##): ")
    print()
    while True:
        if TradeIn == '':
            print('ERROR: The trade in value of your car must be entered')
            print()
            TradeIn = input('Enter the trade in value of your car (#####.##): ')
            print()
        elif TradeIn.isalpha() == True or TradeIn.isspace() == True:
            print('ERROR: The trade in value you entered is invalid')
            print('NOTE: Enter only the numeric value, do not add any spaces or extra characters other than a decimal')
            print()
            TradeIn = input('Enter the trade in value of your car (#####.##): ')
            print()
        elif float(TradeIn) >= SellPrice:
            print('ERROR: The trade in value cannot exceed the sale price')
            print()
            TradeIn = input('Enter the trade in value of your car (#####.##): ')
            print()
        else:
            TradeIn = float(TradeIn)
            break


    SalesName = input("Enter the name of the salesperson: ")
    print()
    ''''''
    # Calculations #

    AfterTrade = SellPrice - TradeIn

    if SellPrice >= 5001:
        LicFee = SellPrice + LIC_RATE_BIG
    else:
        LicFee = SellPrice + LIC_RATE_SMALL

    TranFee = SellPrice * TRAN_RATE
    if SellPrice >= 20000:
        TranFee = TranFee + (SellPrice * LUX_RATE)

    SubTot = AfterTrade + LicFee + TranFee
    HST = SubTot * HST_RATE
    TotSalePrice = SubTot + HST

    

    # Output #

    FirstNameDsp = FirstName[0]

    PhoneNumDsp = '(' + PhoneNum[0:3] + ') ' + PhoneNum[3:6] + '-' + PhoneNum[6:10]

    SellPriceDsp = '${:,.2f}'.format(SellPrice)
    TradeInDsp = '${:,.2f}'.format(TradeIn)

    AfterTradeDsp = '${:,.2f}'.format(AfterTrade)
    LicFeeDsp = '${:,.2f}'.format(LicFee)
    TranFeeDsp = '${:,.2f}'.format(TranFee)

    SubTotDsp = '${:,.2f}'.format(SubTot)
    HSTDsp = '${:,.2f}'.format(HST)

    TotSalePriceDsp = '${:,.2f}'.format(TotSalePrice)

    InvoiceDate1 = CUR_DATE.strftime('%B %d, %Y')
    RecieptNum = FirstName[0] + LastName[0] + '-' + Plate2 + '-' + PhoneNum[6:10]

    InvoiceDate2 = CUR_DATE.strftime('%d-%b-%y')

    FirstPayDate = CUR_DATE + datetime.timedelta(days = 30)
    FirstPayDsp = FirstPayDate.strftime('%d-%b-%y')

    print(f'Honest Harry Car Sales                            Invoice Date:  {InvoiceDate1:>12s}')
    print(f'Used Car Sale and Receipt                         Receipt No:      {RecieptNum:>11s}')
    print()
    print(f'                                         Sale price:                {SellPriceDsp:>10s}')
    print(f'Sold to:                                 Trade Allowance:           {TradeInDsp:>10s}')
    print(f'                                         -------------------------------------')
    print(f'     {FirstNameDsp}. {LastName:<26s}       Price after Trade:         {AfterTradeDsp:>10s}')
    print(f'     {PhoneNumDsp}                      License Fee:               {LicFeeDsp:>10s}')
    print(f'                                         Transfer Fee:              {TranFeeDsp:>10s}')
    print(f'                                         -------------------------------------')
    print(f'Car Details:                             Subtotal:                  {SubTotDsp:>10s}')
    print(f'                                         HST:                       {HSTDsp:>10s}')
    print(f'     {CarYear} {CarMake:<13s} {CarModel:<10s}       -------------------------------------')
    print(f'                                         Total sales price:         {TotSalePriceDsp:>10s}')
    print()
    print(f'------------------------------------------------------------------------------')
    print()
    print()
    print(f'                                 Financing       Total        Monthly')
    print(f'     # Years     # Payments         Fee          Price        Payment')
    print(f'     -----------------------------------------------------------------')
    
    # Payment Loop #
    
    for Year in range (1,5):
        NumPayment = Year * 12

        FinanceFee = Year * FINANCE_RATE
        TotPrice = TotSalePrice + FinanceFee
        MonPayment = TotPrice / NumPayment

        FinanceFeeDsp = '${:,.2f}'.format(FinanceFee)
        TotPriceDsp = '${:,.2f}'.format(TotPrice)
        MonPaymentDsp = '${:,.2f}'.format(MonPayment)

        print(f'         {Year}            {NumPayment}           {FinanceFeeDsp:<7s}     {TotPriceDsp:<10s}    {MonPaymentDsp:<9s}')

    print(f'     -----------------------------------------------------------------')
    print(f'     Invoice date: {InvoiceDate2}         First payment date:{FirstPayDsp}')
    print()
    print(f'----------------------------------------------------------------------')
    print(f'                    Best used cars at the best prices!')
    print()