# lab2_Q3
# ################################################################################
# The following code is given to you.
def print_pattern(my_str, delimiter_str, n):
    """
    This function prints the specified my_str for n times, where every two
    consecutive my_str are separated by the specified delimiter_str. 
    For example, if my_str is "abc", delimiter_str is "-" and n is 3, then the
    pattern being printed is "abc-abc-abc".
    
    Parameters:
        - my_str: The string that's being repeatedly printed.
        - delimiter_str: A string that serves as a delimiter.
        - n: An integer indicating how many times my_str is being printed.
    """
    print(my_str, end='')
    for i in range(n-1):
        print(delimiter_str, end='')
        print(my_str, end='')
    print()

########################################################
# Write your code below to print out the correct output.

# help(print_pattern)
space=' ';

print_pattern("SMU", " * ", 10)
print_pattern("* PYTHON *", "*", 10)
print()
print_pattern("*", space, 4)
print_pattern(space + "*", "", 3)
print_pattern("*", space, 4)
print_pattern(space + "*", "", 3)
print_pattern("*", space, 4)