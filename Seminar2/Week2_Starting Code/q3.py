# ################################################################################
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


# ################################################################################

# ################################################################################
# This function is for you to implement!
def print_signage(msg, symbol):
    # Write your code below to print out the correct output.
    propMsg = symbol + " " + msg + " " + symbol
    print_a_customized_line(symbol, len(propMsg))
    print(propMsg)
    print_a_customized_line(symbol, len(propMsg))


# ################################################################################
# The code below is to test your implementation above.
# DO NOT MODIFY THE CODE BELOW!

print_signage("Hello!", "*")
print()
print_signage("Welcome to SMU", "#")
# ################################################################################
