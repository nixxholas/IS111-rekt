def get_sum_of_digits(my_str):
    digits = "0123456789"
    total = 0
    for char in my_str:
        if char in digits:
            total += int(char)

    return total
