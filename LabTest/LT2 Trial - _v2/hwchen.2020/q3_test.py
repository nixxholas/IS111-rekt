from q3 import check_age

print("Test Case for Q3")
print()

# Test cases used to test your function

print('\nTestcase 1')
print('-' * 10)
my_list = [('John', 'M', '21'), ('Kate', 'F', '19'), ('Eric', 'M', '23')]
print("Expected: True")
print('Actual:   ' + str(check_age(my_list)))

print('\nTestcase 2')
print('-' * 10)
my_list = [('John', 'M', '21'), ('Kate', 'F', '19'), ('Jerry', 'M', '19')]
print("Expected: False")
print('Actual:   ' + str(check_age(my_list)))

print('\nTestcase 3')
print('-' * 10)
my_list = [('Kate', 'F', '19')]
print("Expected: True")
print('Actual:   ' + str(check_age(my_list)))