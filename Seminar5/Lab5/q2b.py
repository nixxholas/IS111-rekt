### Q2 List of Numbers
## b)
# Write your code below:
##############################################################
def all_older_than(age_list, n):
    """
    The function takes two parameters: (1) A list of integers called age_list,
    where each element indicates the age of a person.
    (2) An integer called n, which is a threshold.

    The function returns True if ALL the age values in age_list are larger than n, and False otherwise.
    """

    return True if len(age_list) == 0 else False if age_list[(len(age_list) - 1)] <= n \
        else all_older_than(age_list[:-1], n)


##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: True')
print('Actual:   ' + str(all_older_than([24, 36, 45, 21], 20)))

print('\nTest Case 2')
print('-' * 11)
print('Expected: False')
print('Actual:   ' + str(all_older_than([24, 36, 45, 21], 23)))