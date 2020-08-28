# lab2_Q2
# ##################################################
# The code below is given. 
def display_numbers(m, n):
    """
    This function displays all the integers between m and n sequentially in one row, with
    a space between each two consecutive numbers.
    For example, if m is 3 and n is 5, then this function prints out "3 4 5".
    
    Parameter:
        - m: The starting number.
        - n: The end number.
    """
    for i in range(m, n + 1):
        print(i, end=' ')
    print()

# ##########################################################
# You can use the help() function below to get the 
# description of the above function (which is in the triple 
# quotes and which is called docstring).
# Run the code to see what happens:
# ##########################################################

help(display_numbers)

# ##########################################################
# The code below is given. Try to see what happens 
# when you uncomment the given function with the values 3 and 5.
# ##########################################################

display_numbers(3, 5)

############################################################
# Write your codes below to print the expected output.

display_numbers(0, 10)
display_numbers(5, 9)
