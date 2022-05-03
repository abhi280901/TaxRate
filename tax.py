income = int(input('Please enter your salary:'))
if income <= 5000:
    ttp = 0
    atr = 0
elif 5001 <= income <= 20000:
    ttp = (income-5000)*(1/100)
elif 20001 <= income <= 35000:
    ttp = 150 + (income-20000)*(3/100)
elif 35001 <= income <= 50000:
    ttp = 600 + (income-35000)*(8/100)
elif 50001 <= income <=  70000:
    ttp = 1800 + (income - 50000) * (14 / 100)
elif 70001 <= income <= 100000:
    ttp = 4600 + (income - 70000) * (21 / 100)
elif 100001 <= income <= 250000:
    ttp = 10900 + (income - 100000) * (24 / 100)
elif 250001 <= income <= 400000:
    ttp = 46900 + (income - 250000) * (24.5 / 100)
elif 400001 <= income <= 600000:
    ttp = 83650 + (income - 400000) * (25 / 100)
elif 600001 <= income <= 1000000:
    ttp = 133650 + (income - 600000) * (26 / 100)
elif 1000001 <= income <= 2000000:
    ttp = 237650 + (income - 1000000) * (28 / 100)
else:
    ttp = 517650 + (income - 2000000) * (30 / 100)

atr = ttp/income
print("Your Average Tax Rate(ATR) is "+ str(atr) + "%!")
print("Total amount of tax to be paid is RM"+ str(ttp) + '!')
print("Thank you!:)")