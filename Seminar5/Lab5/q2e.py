### Q2 List of Numbers
## e)
# Write your code below:
##############################################################
def calculate_sums(num_list):
    if (len(num_list) == 0) or (len(num_list) == 1): return num_list

    sum_list = []
    # Iterate the number list, ensuring every number is iterated systematically
    for i in range(0, len(num_list)):
        # Assign two vars, Value (Stores the total value for the upcoming element) and
        # Index (Pointer till the target index)
        val, index = 0, 0
        while index < i + 1:
            val += num_list[index]
            index += 1
        sum_list.append(val)

    return sum_list


##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: [2, 5, 11, 12, 17]')
print('Actual:   ' + str(calculate_sums([2, 3, 6, 1, 5])))

print('\nTest Case 2')
print('-' * 11)
print('Expected: []')
print('Actual:   ' + str(calculate_sums([])))