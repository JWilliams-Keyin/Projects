# Description: This program calculates the monthly and yearly prices of yacht sites for members
#              of the St. John's Marina & Yacht Club
# Author:      Jack Williams
# Date:        May 27th - May 31st

# Program Constants #

EVEN_PRICE = 80.00
ODD_PRICE = 120.00
ALT_MEM_RATE = 5.00
CLEAN_PRICE = 50.00
SURV_PRICE = 35.00
HST_RATE = 0.15
STAND_DUES = 75.00
EXEC_DUES = 150.00
PROC_FEE = 59.99
CANCEL_RATE = 0.40

# User Input Values #

print()
print("St. John's Marina & Yacht Club" )
print()
print('Please enter the following values:')
print()
Date = input('Date (YYYY-MM-DD): ')
print()
SiteNum = int(input('Site Number (1-100): '))
print()
MemName = input('Name: ')
StrAdd = input('Street Address: ')
City = input('City: ')
Prov = input('Province (Initials): ')
PostCode = input('Postal Code: ')
PhoneNum = input('Home Phone Number (+#-###-####)')
CellNum = input('Cell Phone Number (+#-###-####)')
print()
MemType = input('Type of Membership (S or E): ')
AltMem = int(input('Number of Alternate Members: '))
SiteClean = input('Site Cleaning (Y or N): ')
VidSurv = input('Video Surveillance (Y or N): ')

# Calculations #

if SiteNum == (SiteNum//2*2):
    SiteCost = EVEN_PRICE
else:
    SiteCost = ODD_PRICE

if SiteClean == str('Y'):
    FinalClean = CLEAN_PRICE
    SiteCleanDsp = str('Yes')
else:
    FinalClean = 0
    SiteCleanDsp = str('No')

if VidSurv == str('Y'):
    FinalSurv = SURV_PRICE
    VidSurvDsp = str('Yes')
else:
    FinalSurv = 0
    VidSurvDsp = str('No')

AltMemPrice = ALT_MEM_RATE * AltMem
SiteCharge = SiteCost + AltMemPrice
ExtraCharge = FinalClean + FinalSurv

SubTot = SiteCharge + ExtraCharge
HST = SubTot * HST_RATE
MonCharge = SubTot + HST

if MemType == str('E'):
    MonDues = EXEC_DUES
    MemTypeDsp = str('Executive')
else:
    MonDues = STAND_DUES
    MemTypeDsp = str('Standard')

TotMonFees = MonCharge + MonDues
TotYearFees = TotMonFees * 12

MonPayment = (TotYearFees + PROC_FEE) /12
CancelFee = (SiteCharge * 12) * CANCEL_RATE

# Output #

print()
print(f"   St.John's Marina & Yacht Club")
print(f"       Yearly Member Reciept")
print()
print(f'____________________________________')
print()
print(f'Client Name and Address:')
print()
print(f'{MemName:<24s}')
print(f'{StrAdd:<24s}')
print(f'{City}, {Prov} {PostCode:<6s}')
print()
print(f'Phone: {PhoneNum} (H)')
print(f'       {CellNum} (C)')
print()
print(f'Site #: {SiteNum:<3} Member type: {MemTypeDsp}')
print()
print(f'Alternate Members:                {AltMem:>2}')
print(f'Weekly Site Cleaning:            {SiteCleanDsp:>3s}')
print(f'Video Surveillance:              {VidSurvDsp:>3s}')
print()
SiteChargeDsp = '${:,.2f}'.format(SiteCharge)
ExtraChargeDsp = '${:,.2f}'.format(ExtraCharge)

SubTotDsp = '${:,.2f}'.format(SubTot)
HSTDsp = '${:,.2f}'.format(HST)

MonChargeDsp = '${:,.2f}'.format(MonCharge)
MonDuesDsp = '${:,.2f}'.format(MonDues)

TotMonFeesDsp = '${:,.2f}'.format(TotMonFees)
TotYearFeesDsp = '${:,.2f}'.format(TotYearFees)

MonPaymentDsp = '${:,.2f}'.format(MonPayment)

CancelFeeDsp = '${:,.2f}'.format(CancelFee)
print(f'Site Charges:                {SiteChargeDsp:>6s}')
print(f'Extra Charges:                {ExtraChargeDsp:>5s}')
print('                       -------------')
print(f'Subtotal:                    {SubTotDsp:>6s}')
print(f'Sales Tax (HST):              {HSTDsp:>5s}')
print('                       -------------')
print(f'Total Monthly Charges:       {MonChargeDsp:>6s}')
print(f'Monthly Dues:                {MonDuesDsp:>5s}')
print('                       -------------')
print(f'Total Monthly Fees:          {TotMonFeesDsp:>6s}')
print(f'Total Yearly Fees:         {TotYearFeesDsp:>7s}')
print()
print(f'Monthly Payment:             {MonPaymentDsp:>6s}')
print()
print('____________________________________')
print()
print(f'Issued: {Date}')
print('HST Reg No: 549-33-5849-4720-9885')
print()
print(f'Cancellation Fee:            {CancelFeeDsp:>6s}')