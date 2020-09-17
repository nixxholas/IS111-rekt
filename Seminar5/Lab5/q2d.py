### Q2 List of Numbers
## d)
# Write your code below:
##############################################################
def get_prime_numbers(num_list, sep):
    res = ''
    while len(num_list) > 0:
        num = num_list.pop(0)
        if is_prime(num):
            res += str(num) + sep
    return res[:-1]


def is_prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0: return False
        return True
    return False

##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: 2-7-11-19')
print('Actual:   ' + str(get_prime_numbers([2, 4, 7, 9, 11, 16, 19, 21], '-')))

print('\nTest Case 2')
print('-' * 11)
print('Expected: 3')
print('Actual:   ' + str(get_prime_numbers([3, 4, 8, 9, 12, 16], '*')))
