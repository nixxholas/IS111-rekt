# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def get_sum_of_digits(my_str):
    total = 0

    for c in my_str:
        if c.isnumeric(): total += int(c)

    return total
