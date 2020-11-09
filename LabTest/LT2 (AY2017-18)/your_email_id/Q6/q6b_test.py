from q6b import get_all_permutations

print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()

my_list = get_all_permutations('abc')
print("Expected: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']")
print("      or: the elements above in a different order")
print("Actual  : " + str(my_list))
print()
print("Expected type of returned value: <class 'list'>")
print("Actual type of returned value  : " + str(type(my_list)))
print()
print("====================")
print()

# Test Case 2:
print("Test Case #2:")
print()

my_list = get_all_permutations('ab')
print("Expected: ['ab', 'ba']")
print("      or: the elements above in a different order")
print("Actual  : " + str(my_list))
print()
print("====================")
print()

# Test Case 3:
print("Test Case #3:")
print()

my_list = get_all_permutations('aab')
print("Expected: ['aab', 'aba', 'baa']")
print("      or: the elements above in a different order")
print("Actual  : " + str(my_list))
print()
print("====================")
print()

# Test Case 4:
print("Test Case #4:")
print()

my_list = get_all_permutations('a')
print("Expected: ['a']")
print("Actual  : " + str(my_list))
print()
print("====================")
print()