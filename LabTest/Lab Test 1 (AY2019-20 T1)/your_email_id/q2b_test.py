from q2b import add_even_numbers

print()
print('-' * 20)
print()

print("Test Case 1: add_even_numbers(['1|2|3', '10|50']))")

print()

result = add_even_numbers(['1|2|3', '10|50'])
print('Expected: 62')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: add_even_numbers(['99|1|27', '11|5'])")

print()

result = add_even_numbers(['99|1|27', '11|5'])
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 3: add_even_numbers(['1', '12'])")

print()

result = add_even_numbers(['1', '12'])
print('Expected: 12')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 4: add_even_numbers([])")

print()

result = add_even_numbers([])
print('Expected: 0')
print('Actual:   ' + str(result))