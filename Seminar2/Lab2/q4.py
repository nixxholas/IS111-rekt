#Lab2_Q4
# #####################################
# Write your code below to first define 
# the function calculate_interest()

def calculate_interest(principal, annual_interest_rate, frequency_of_compounding, deposit_rate):
    return 0


# ################################################################
# The default annual interest rate of 0.5%, compounded 
# monthly, has been provided for you.

# Annual interest rate (which is fixed)
ANNUAL_INTEREST_RATE = 0.005
# Number of times the interest is compounded per year
FREQUENCY_OF_COMPOUNDING = 12

# ################################################################
# Write your code below to prompt the user and display the 
# interest earned.

print("The interest you will earn is", calculate_interest(float(input("What's the amount of your principal? "),
                                                                ANNUAL_INTEREST_RATE, FREQUENCY_OF_COMPOUNDING,
                                                                float(input("How many years do you want to deposit "
                                                                            "the money? ")))))


