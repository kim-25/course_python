"""
Your job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""
###Solucion
bill=0


size = input("What is the size?: small (S), Medium (M), large (L): ")
pepperoni = bool(input('Do yuo want to add pepperoni?: (1) yes, (0) No :   '))
cheese = bool(input('Do yuo want to add cheese?: (1) yes, (0) No :   '))
if size == 'S':
    bill +=15  #bill+=15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25


if size == 'S' and pepperoni =='1':
    bill += 2
elif pepperoni:
    bill += 3

if cheese == '1':
    bill += 1
else:
    bill +=0

print(bill)