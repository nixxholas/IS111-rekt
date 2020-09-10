## Q3 PART 1
# This function is for you to implement!
def calculate_salary(monthly_sales):
    # This variable is defined for you to use.
    SALARY = 2000.0

    # ################################################################################
    # Modify the code below to return the right amount of salary.
    if monthly_sales >= 18000:
        SALARY += (monthly_sales * 0.18)
    elif monthly_sales >= 15000:
        SALARY += (monthly_sales * 0.15)
    elif monthly_sales >= 10000:
        SALARY += (monthly_sales * 0.1)
    elif 10000 > monthly_sales > 0:
        SALARY += (monthly_sales * 0.05)

    return SALARY
    # ################################################################################


## Q3 PART 2
# Write your code below
print("The monthly pay for the salesperson is $"
      + str(calculate_salary(float(input("Enter monthly sales amount($): ")))))
