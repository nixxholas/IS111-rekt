from q2 import get_sum_of_odd_numbers

print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
my_list = [9, 4, 6, 7]
my_sum = get_sum_of_odd_numbers(my_list)
print("Expected: 16")
print("Actual  : " + str(my_sum))
print()
print("Expected type of returned value: <class 'int'>")
print("Actual type of returned value  : " + str(type(my_sum)))
print()
print("====================")
print()


# Test Case 2:
print("Test Case #2:")
print()
my_list = [4, 13, 8, 12]
my_sum = get_sum_of_odd_numbers(my_list)
print("Expected: 13")
print("Actual  : " + str(my_sum))
print()
print("====================")
print()

# Test Case 3:
print("Test Case #3:")
print()
my_list = [6, 18, 44]
my_sum = get_sum_of_odd_numbers(my_list)
print("Expected: 0")
print("Actual  : " + str(my_sum))
print()
print("====================")
print()

# Test Case 4:
print("Test Case #4:")
print()
my_list = []
my_sum = get_sum_of_odd_numbers(my_list)
print("Expected: 0")
print("Actual  : " + str(my_sum))
print()
print("====================")
print()