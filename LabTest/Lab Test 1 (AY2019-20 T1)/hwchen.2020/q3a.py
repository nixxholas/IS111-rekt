# Name: Nicholas Chen
# Email ID: hwchen.2020

def calculate_entrance_fees_1(n):
    # These variables are defined for you to use.
    PACKAGE_B = 110
    PACKAGE_C = 200

    # Modify the code below.
    total = 0

    if n <= 1: return n * PACKAGE_B

    while n > 0:
        if n - 2 >= 0:
            total += PACKAGE_C
            n -= 2
        elif n - 1 >= 0:
            total += PACKAGE_B
            n -= 1

    return total
