### Q3 Shopping Cart
## b)
# Write your code below:
##############################################################










##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
item_list = [("milk", 5.45, 2), ("eggs", 2.45, 1), ("shampoo", 8.90, 2)]
print("Expected: ['milk', 'eggs', 'shampoo']")
print('Actual:   ' + str(get_items(item_list)))

print('\nTest Case 2')
print('-' * 11)
item_list = []
print("Expected: []")
print('Actual:   ' + str(get_items(item_list)))