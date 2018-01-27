balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
lower = balance / 12.0
upper = balance * ( 1 + monthlyInterestRate) ** 12 / 12.0
mp = round((lower + upper)/2, 2)
mp_old = 0

while mp != mp_old:
    b = balance
    for i in range(12):
        ub = b - mp
        b = ub + annualInterestRate / 12.0 * ub
        if b < 0:
            break
    if b < 0:
        upper = mp
    else:
        lower = mp
    mp_old = mp
    mp = round((lower + upper)/2, 2)

if b > 0:
    mp = mp + 0.01
    
print("Lowest Payment: {}".format(round(mp,2)))

