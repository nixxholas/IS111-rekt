def calculate_income_tax(annual_income):
    taxable = 0
    if annual_income >= 320000:
        taxable += 44550
        if (annual_income - 320000) > 0:
            taxable += (annual_income - 320000) * 22 / 100
    elif annual_income >= 280000:
        taxable += 36550
        if (annual_income - 280000) > 0:
            taxable += (annual_income - 280000) * 20 / 100
    elif annual_income >= 240000:
        taxable += 28750
        if (annual_income - 240000) > 0:
            taxable += (annual_income - 240000) * 19.5 / 100
    elif annual_income >= 200000:
        taxable += 21150
        if (annual_income - 200000) > 0:
            taxable += (annual_income - 200000) * 19 / 100
    elif annual_income >= 160000:
        taxable += 13950
        if (annual_income - 160000) > 0:
            taxable += (annual_income - 160000) * 18 / 100
    elif annual_income >= 120000:
        taxable += 7950
        if (annual_income - 120000) > 0:
            taxable += (annual_income - 120000) * 15 / 100
    elif annual_income >= 80000:
        taxable += 3350
        if (annual_income - 80000) > 0:
            taxable += (annual_income - 80000) * 11.5 / 100
    elif annual_income >= 40000:
        taxable += 550
        if (annual_income - 40000) > 0:
            taxable += (annual_income - 40000) * 7 / 100
    elif annual_income >= 30000:
        taxable += 200
        if (annual_income - 30000) > 0:
            taxable += (annual_income - 30000) * 3.5 / 100
    elif (annual_income - 20000) > 0:
        taxable += (annual_income - 20000) * 2 / 100

    return taxable


print("Your total tax is $", calculate_income_tax(float(input("Enter your annual taxable income: "))))
