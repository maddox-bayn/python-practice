income = float(input(10000))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income-85528) * 0.32 + 14839.02

    if tax < 0.0:
        tax = 0.0
        tax = round(tax, 0)
        print("the tax is", tax, "thelers")