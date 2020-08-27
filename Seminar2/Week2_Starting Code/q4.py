# ################################################################################
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
# ################################################################################


# You can verify your answers to Q4 by printing out the values of the function calls below.

# 130
print(calculate_total_amount(2, 3))
# 150
print(calculate_total_amount(2, 3, 4))
# 152
print(calculate_total_amount(2, 3, 4, 1))
# 155
print(calculate_total_amount(2, 3, 4, 1, 3))
# 138
print(calculate_total_amount(2, 3, two_note=4))
# 143
print(calculate_total_amount(2, 3, two_note=4, five_note=1))
# Ten note is missing, error.
print(calculate_total_amount(3, two_note=4, five_note=1))