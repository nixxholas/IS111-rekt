# ################################################################################
# This function is for you to implement!
def calculate_tax_3(income):
    """
    This function assumes that the income is between $0 and $40,000.
    """
    # If u ain't earning, get lost or if u earning beyond 40k
    if income <= 0:
        return Exception("Don't be broke.")

    # 20k <
    if income <= 20000:
        return 0

    # 20 - 30k
    if income <= 30000:
        return (income - 20000) * 0.02

    # Since the last bit are for 40k and below,
    return 200 + ((income - 30000) * 0.035)

# ################################################################################

# Call the function above to test whether it works.
print(calculate_tax_3(25000.0))
print(calculate_tax_3(10000.0))
print(calculate_tax_3(35000.0))

# ################################################################################
