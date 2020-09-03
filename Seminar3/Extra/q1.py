def compute_factorial(n):
    return n * compute_factorial(n - 1) if n > 1 else n


def get_num_digits(n):
    return 1 if n < 10 else 1 + get_num_digits(n / 10)


def display_fibonacci_numbers(n):
    if n <= 1:
        return n
    else:
        return display_fibonacci_numbers(n - 1) + display_fibonacci_numbers(n - 2)


# print(compute_factorial(5))
# print(get_num_digits(400000))

for i in range(1, 6):
    print(display_fibonacci_numbers(i), end=' ')
