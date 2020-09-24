# Name: Nicholas Chen
# Email ID: hwchen.2020

import q3a

def calculate_entrance_fees_2(m, n):
    # These variables are defined for you to use.
    ADULT_TICKET = 75
    CHILD_TICKET = 50
    
    PACKAGE_A = 140
    PACKAGE_B = 110
    PACKAGE_C = 200

    # Modify the code below.
    # Find the minimum pax between adults and children.
    total = 0
    min_val = min(m, n)
    if min_val > 0:
        total += q3a.calculate_entrance_fees_1(min_val)
        m -= min_val
        n -= min_val

    total += (CHILD_TICKET * n)

    while m > 0:
        if m >= 2:
            total += PACKAGE_A
            m -= 2
        elif m == 1:
            total += ADULT_TICKET
            m -= 1

    return total
 