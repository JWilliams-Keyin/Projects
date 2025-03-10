ItemName = input('Enter the item name: ')
ItemCost = float(input('Enter the item cost: '))
NumInStock = int(input('Enter the number of items in stock: '))

RetailPrice = ItemCost * 1.75
TotInvCost = ItemCost * NumInStock
TotInvRetail = RetailPrice * NumInStock
GrossMargin = TotInvRetail - TotInvCost
Sale10Off = RetailPrice * 0.90
Sale25Off = RetailPrice * 0.75
Sale33Off = RetailPrice * 0.67
Sale50Off = RetailPrice * 0.50

print('Item name: ', ItemName)
print('Item cost: $', ItemCost)
print('Number in stock: ', NumInStock)
print('Retail price: $', RetailPrice)
print('Total inventory at cost: $', TotInvCost)
print('Total inventory at retail: $', TotInvRetail)
print('Gross margin: $', GrossMargin)
print('10% off price: $', Sale10Off)
print('25% off price: $', Sale25Off)
print('33% off price: $', Sale33Off)
print('50% off price: $', Sale50Off)