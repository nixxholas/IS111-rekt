# ################################################################################
# This function is for you to implement!
def calculate_tax_1(income):
    """
    This function assumes that the income is between $20,000 and $30,000.
    """
    # If u ain't earning 20-30k, get lost
    if income < 20000 or income > 30000:
        return Exception("Invalid income range.")

    # Modify the code below to return the right amount of tax.
    return (income - 20000) * 0.02


# ################################################################################

# Call the function above to test whether it works.
print(calculate_tax_1(25000.0))
