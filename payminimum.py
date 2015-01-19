balance = 
annualInterestRate = 
monthlyPaymentRate = 

previousbal = balance
mointerate = annualInterestRate/12
monthnum = 1
paidup = 0

while monthnum <= 12:
    #calculat min payment
    minmopay = monthlyPaymentRate * previousbal
    paidup += minmopay
    #calc monthly unpaid balance
    monunpabal = previousbal - minmopay
    #calc update monthly bal
    updatedbalmo = previousbal + (mointerate *  monunpabal)
    previousbal = updatedbalmo - minmopay
    
    print('Month:' + str(monthnum))
    print('Minimum monthly payment: ' + str(round(minmopay,2)))
    print('Remaining balance: ' + str(round(previousbal,2)))
    monthnum += 1
    
print('Total paid: ' + str(round(paidup,2)))
print('Remaining balance: ' + str(round(previousbal,2)))