## Q8
# ################################################################################
# The function below is for you to implement!
def display_fibonacci(n):
    """
    This function takes in an integer n (greater or equal to 3). It prints out the 
    first n Fibonacci numbers, starting from 1. The function doesn’t return anything.
    """
    # Modify the code below to print the first n Fibonacci numbers
    for i in range(1, n + 1):
        # print("(" + str(i) + ")", end= ' ')
        if i <= 1:
            print(i, end=' ')
        else:
            print(i - 1 + i - 2, end=' ')
    print()
