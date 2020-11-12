from q1 import count_long_strings

print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
my_list = ["apple", "orange", "pear"]
my_count = count_long_strings(my_list)
print("Expected: 2")
print("Actual  : " + str(my_count))
print()
print("Expected type of returned value: <class 'int'>")
print("Actual type of returned value  : " + str(type(my_count)))
print()
print("====================")
print()

# Test Case 2:

print("Test Case #2:")
print()
my_list = ["", "S M U", "SMU"]
my_count = count_long_strings(my_list)
print("Expected: 1")
print("Actual  : " + str(my_count))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
my_list = []
my_count = count_long_strings(my_list)
print("Expected: 0")
print("Actual  : " + str(my_count))
print()
print("====================")
print()