from q2 import get_reversed_list

# #####################################
# Test Cases of Q2

print('\nTestcase 1')
print('-' * 10)
my_list = [1.5, 2.5, 3.9]
print("Expected: [-3.9, -2.5, -1.5]")
print('Actual:   ' + str(get_reversed_list(my_list)))

print('\nTestcase 2')
print('-' * 10)
my_list = [4.5, 0.0]
print("Expected: [0.0, -4.5]")
print('Actual:   ' + str(get_reversed_list(my_list)))

print('\nTestcase 3')
print('-' * 10)
my_list = []
print("Expected: []")
print('Actual:   ' + str(get_reversed_list(my_list)))