# Q1a ################################################################################
# The following code is given to you.
def compute_average(a, b, c):
    """
    This function returns the average of the three numbers a, b and c.
    """
    return (a + b + c)/3

# Write your code below:
n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
n3 = float(input("Enter 3rd number: "))

avg = compute_average(n1, n2, n3)
print("Average:", avg)

# Q1b ################################################################################
# Implement the function below:
def compute_geometric_mean(x, y, z):
    """
    This function returns the geometric mean of the three numbers x, y and z.
    """
    # Write your code here:
    
    return (x * y * z) ** (1/3)

# The code below is to test your implementation above.
# DO NOT MODIFY THE CODE BELOW!
print("The geometric mean of 2, 4 and 6 is:", compute_geometric_mean(2, 4, 6))

# Q2 ################################################################################
# The following code is given to you.
def print_a_line():
    """
    This function displays a line of 20 dashes.
    """
    print("--------------------")
    
def print_a_message(msg, symbol):
    """
    This function displays a given text message enclosed in a pair of the specified symbols.
    For example, if msg is "Welcome" and symbol is "#", then the function displays "# Welcome #".
    
    Parameters:
      - msg: A string that represents the text message to be displayed.
      - symbol: A single character that is used to enclose the text message.
    """
    print(symbol + " " + msg + " " + symbol)
    
# Write your code below:
print_a_line()
print_a_message('Hello SIS!', '|')
print_a_line()

print_a_line()
print_a_message('Hello Python!', '*')
print_a_message('Hello Functions!', '$')
print_a_line()

# Q3 ################################################################################
# The following code is given to you.
def print_a_customized_line(symbol, n):
    """
    This function prints the specified symbol n times in the same row.
    For example, if symbol is '*' and n is 5, the function prints '*****'.
    
    Parameters:
        - symbol: The symbol to be repeated.
        - n: The number of times the symbol is to be repeated.
    """
    for i in range(n):
        print(symbol, end='')
    print()

# This function is for you to implement!
def print_signage(msg, symbol):
    
    # Write your code below to print out the correct output.

    print_a_customized_line(symbol, len(msg) + 4)
    print_a_message(msg, symbol)
    print_a_customized_line(symbol, len(msg) + 4)
    
# The code below is to test your implementation above.
# DO NOT MODIFY THE CODE BELOW!
print_signage("Hello!", "*")
print()
print_signage("Welcome to SMU", "#")

# Q4 ################################################################################
# The following code is given to you.
def calculate_total_amount(fifty_note, ten_note, five_note=0, two_note=0, one_coin=0):
    """
    This function takes in five parameters representing the numbers of banknotes and coin of
    different denominations received. The function returns the total amount of money.
    Parameters:
        - fifty_note: The number of fifty-dollar notes.
        - ten_note: The number of ten-dollar notes.
        - five_note: The number of five-dollar notes.
        - two_note: The number of two-dollar notes.
        - one_coin: The number of one-dollar coins.
    Return:
        The total amount in dollars of the notes and coins passed in.
    """
    return fifty_note * 50 + ten_note * 10 + five_note * 5 + two_note * 2 + one_coin

# You can verify your answers to Q4 by printing out the values of the function calls below.
print(calculate_total_amount(2, 3))
print(calculate_total_amount(2, 3, 4))
print(calculate_total_amount(2, 3, 4, 1))
print(calculate_total_amount(2, 3, 4, 1, 3))
print(calculate_total_amount(2, 3, two_note=4))
print(calculate_total_amount(2, 3, two_note=4, five_note=1))
print(calculate_total_amount(3, two_note=4, five_note=1))

# Q5a ################################################################################
# Write your code below.
import math

size = float(input("What's the size of the square (in square centimeters)? "))
side = math.sqrt(size)
print("Each side of this square is " + str(side) + " centimeters.")


# Q5b ################################################################################
# Write your code below.

import random

num = int(input("Enter a positive integer: "))
rand_num = random.randint(1, num)
print(rand_num)

# Q6 ################################################################################
import week2_utility

age = int(input("What's your age? "))
gender = input("What's your gender [M|F] :")

premium = week2_utility.get_insurance_premium(age, gender)
print("Your premium is $" + str(premium))

# Q7 ################################################################################
# This line of code prompts the user for a system time.
input_str = input('Please enter the system time (in seconds): ')

# Modify the code below to get the correct numbers of days, hours, minutes and seconds.

num_days = 0
num_hours = 0
num_minutes = 0
num_seconds = 0

# Q7 - Solution 1:
NUM_SECONDS_PER_MINUTE = 60
NUM_SECONDS_PER_HOUR = 60 * 60
NUM_SECONDS_PER_DAY = 60 * 60 * 24

total_num_seconds = int(input_str)

num_days = total_num_seconds // NUM_SECONDS_PER_DAY
num_seconds_left = total_num_seconds % NUM_SECONDS_PER_DAY

num_hours = num_seconds_left // NUM_SECONDS_PER_HOUR
num_seconds_left = num_seconds_left % NUM_SECONDS_PER_HOUR

num_minutes = num_seconds_left // NUM_SECONDS_PER_MINUTE
num_seconds = num_seconds_left % NUM_SECONDS_PER_MINUTE

# DO NOT MODIFY THE CODE BELOW!!!
# This line of code displays the results.
print('Based on this system time, ' + str(num_days) + ' days, ' + str(num_hours) + ' hours, ' + str(num_minutes) + ' minutes and ' + str(num_seconds) + ' seconds have passed since 1 January 1970 00:00:00 UT.') 

# Q7 - Solution 2:
# num below is the total number of seconds
num = int(input_str)
num_seconds = num % 60
# num below is the remaining number of minutes (after num_seconds above is excluded)
num = num // 60
num_minutes = num % 60
# num below is the ramaining number of hours (after num_minutes above is excluded)
num = num // 60
num_hours = num % 24
num_days = num // 24

# DO NOT MODIFY THE CODE BELOW!!!
# This line of code displays the results.
print('Based on this system time, ' + str(num_days) + ' days, ' + str(num_hours) + ' hours, ' + str(num_minutes) + ' minutes and ' + str(num_seconds) + ' seconds have passed since 1 January 1970 00:00:00 UT.') 

# Q8 ################################################################################
# Q8a - This function is for you to implement!
def calculate_tax_1(income):
    """
    This function assumes that the income is between $20,000 and $30,000.
    """
    
    # Modify the code below to return the right amount of tax.
    
    # return 0.0
    
    return (income - 20000) * 0.02

# Call the function above to test whether it works.
print(calculate_tax_1(25000.0))

# Q8b - This function is for you to implement!
def calculate_tax_2(income):
    """
    This function assumes that the income is between $0 and $30,000.
    """
    
    # Modify the code below to return the right amount of tax.
    
    # return 0

    return max( (income - 20000) * 0.02, 0.0)

# Call the function above to test whether it works.
print(calculate_tax_2(25000.0))
print(calculate_tax_2(10000.0))

# Q8c - This function is for you to implement!
def calculate_tax_3(income):
    """
    This function assumes that the income is between $0 and $40,000.
    """
    
    # Modify the code below to return the right amount of tax.
    
    # return 0

    return max( (income - 30000) * (0.035 - 0.02), 0.0 ) + max( (income - 20000) * 0.02, 0.0 )

# Call the function above to test whether it works.
print(calculate_tax_3(25000.0))
print(calculate_tax_3(10000.0))
print(calculate_tax_3(35000.0))