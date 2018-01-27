balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

b = balance
for i in range(12):
    ub = b * (1 - monthlyPaymentRate)
    b = ub + annualInterestRate / 12.0 * ub
    
print("Remaining balance: {}".format(round(b,2)))
