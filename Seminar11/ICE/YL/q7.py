def get_family_members(family_tree, name):
    pass

family_tree = {}
name = 'Jane'
result = get_family_members(family_tree, name)
print('Test 1')
print('Expected:[]')
print('Actual  :' + str(result))
print()

family_tree = {'Frank': ['Mary', 'Jane'], 'Jane': ['Nick', 'Wendy']}
name = 'Jane'
result = get_family_members(family_tree, name)
print('Test 2')
print("Expected:['Nick', 'Wendy']")
print("Actual  :" + str(result))
print()

family_tree = {'Frank': ['Mary', 'Jane'], 'Jane': ['Nick']}
name = 'Frank'
result = get_family_members(family_tree, name)
print('Test 3')
print("Expected:['Mary', 'Jane', 'Nick']")
print("Actual  :" + str(result))
print()


family_tree = {'Alan': ['Bob'],
               'Bob': ['Chris', 'Eric'],
               'Eric': ['Jim']}
name = 'Alan'
result = get_family_members(family_tree, name)
print('Test 4')
print("Expected:['Bob', 'Chris', 'Eric', 'Jim']")
print("Actual  :" + str(result))
print()

family_tree = {'Alan': ['Bob', 'Eric', 'Hannah'],
               'Bob': ['Chris', 'Debbie'],
               'Debbie': ['Cindy'],
               'Eric': ['Dan', 'Fanny'],
               'Fanny': ['George']}
name = 'Alan'
result = get_family_members(family_tree, name)
print('Test 4')
print("Expected:['Bob', 'Eric', 'Hannah', 'Chris', 'Debbie', 'Dan', 'Fanny', 'Cindy', 'George']")
print("Actual  :" + str(result))
print()

