# Name    :
# Email ID:

# start of answer

def reverse_num(number):
    n_list = list(str(number))
    is_negative = n_list[0] == '-'

    # If its negative,
    if is_negative:
        # Remove the '-'
        n_list.pop(0)

    # Remove trailing zeros
    if len(n_list) > 1:
        while n_list[len(n_list) - 1] == '0':
            n_list.pop()

    return int(("-" + "".join(n_list[::-1])) if is_negative else "".join(n_list[::-1]))

# end of answer

print("Test 1: Test that the return value is an int value")
print("Expected:True")
print("Actual  :" + str(isinstance(reverse_num(123), int)))
print()

print("Test 2")
print("Expected:2017")
print("Actual  :" + str(reverse_num(7102)))
print()

print("Test 3")
print("Expected:32")
print("Actual  :" + str(reverse_num(230)))
print()

print("Test 4")
print("Expected:0")
print("Actual  :" + str(reverse_num(0)))
print()

print("Test 5")
print("Expected:-21")
print("Actual  :" + str(reverse_num(-12)))
print()

