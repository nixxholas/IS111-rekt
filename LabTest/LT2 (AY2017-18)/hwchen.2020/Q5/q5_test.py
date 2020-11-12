from q5 import get_family_members

print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()

family_head = ('Mary', [])
result_list = get_family_members(family_head)
print("Expected: ['Mary']")
print("Actual  : " + str(result_list))
print()
print("Expected type of returned value: <class 'list'>")
print("Actual type of returned value  : " + str(type(result_list)))
print()
print("====================")
print()

# Test Case 2:
print("Test Case #2:")
print()

family_head = ('Jane', [('Nick', []), ('Wendy', [])])
result_list = get_family_members(family_head)
print("Expected: ['Jane', 'Nick', 'Wendy']")
print("Actual  : " + str(result_list))
print()
print("====================")
print()

# Test Case 3:
print("Test Case #3:")
print()

family_head = ('Frank', [('Mary', []), ('Jane', [('Nick', [])])])
result_list = get_family_members(family_head)
print("Expected: ['Frank', 'Mary', 'Jane', 'Nick']")
print("Actual  : " + str(result_list))
print()
print("====================")
print()

# Test Case 4:
print("Test Case #4:")
print()

family_head = ('Alan', [('Bob', [('Chris', [])]), ('Eric', [])])
result_list = get_family_members(family_head)
print("Expected: ['Alan', 'Bob', 'Eric', 'Chris']")
print("Actual  : " + str(result_list))
print()
print("====================")
print()

# Test Case 5:
print("Test Case #5:")
print()

family_head = ('Alan', [('Bob', [('Chris', []), ('Debbie', [('Cindy', [])])]), ('Eric', [('Dan', []), ('Fanny', [('George', [])])]), ('Hannah', [])])
result_list = get_family_members(family_head)
print("Expected: ['Alan', 'Bob', 'Eric', 'Hannah', 'Chris', 'Debbie', 'Dan', 'Fanny', 'Cindy', 'George']")
print("Actual  : " + str(result_list))
print()
print("====================")
print()
