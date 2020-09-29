from q1b import is_compatible

print()
print('-' * 20)
print()

print('Test Case 1: is_compatible("B", "AB")')

print()

result = is_compatible("B", "AB")
print('Expected: True')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: is_compatible("O", "A")')

print()

result = is_compatible("O", "A")
print('Expected: True')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: is_compatible("AB", "O")')

print()

result = is_compatible("AB", "O")
print('Expected: False')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()