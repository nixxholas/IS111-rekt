from q2a import get_number_of_long_strings

print()
print('-' * 20)
print()

print("Test Case 1: get_number_of_long_strings(['123456', 'abc', '++++', '!@#$%'], 4)")

print()

result = get_number_of_long_strings(['123456', 'abc', '++++', '!@#$%'], 4)
print('Expected: 2')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: get_number_of_long_strings(['!!!', 'apple', 'sheep', 'dinosaur', '@'], 6)")

print()

result = get_number_of_long_strings(['!!!', 'apple', 'sheep', 'dinosaur', '@'], 6)
print('Expected: 1')
print('Actual:   ' + str(result))


print()
print('-' * 20)
print()

print("Test Case 3: get_number_of_long_strings(['abcdefg', '1234567890'], 100)")

print()

result = get_number_of_long_strings(['abcdefg', '1234567890'], 100)
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 4: get_number_of_long_strings([''], 1)")

print()

result = get_number_of_long_strings([''], 1)
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 5: get_number_of_long_strings([], 1)")

print()

result = get_number_of_long_strings([], 1)
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()