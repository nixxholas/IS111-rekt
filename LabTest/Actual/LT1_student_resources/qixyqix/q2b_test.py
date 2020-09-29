from q2b import get_max_of_min

print()
print('-' * 20)
print()

print('Test Case 1: get_max_of_min([(1, 5, 3), (5, 1, 9), (4, 10, 19)])')

print()

result = get_max_of_min([(1, 5, 3), (5, 1, 9), (4, 10, 19)])
print('Expected: 4')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: get_max_of_min([(-15, 20, -40), (-4, -1, -4)])')

print()

result = get_max_of_min([(-15, 20, -40), (-4, -1, -4)])
print('Expected: -4')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: get_max_of_min([(3, -9, 0)])')

print()

result = get_max_of_min([(3, -9, 0)])
print('Expected: -9')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 4: get_max_of_min([])')

print()

result = get_max_of_min([])
print('Expected: None')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'NoneType'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()