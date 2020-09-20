from q3a import calculate_entrance_fees_1

print()
print('-' * 20)
print()

print("Test Case 1: calculate_entrance_fees_1(1)")

print()

result = calculate_entrance_fees_1(1)
print('Expected: 110')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: calculate_entrance_fees_1(2)")

print()

result = calculate_entrance_fees_1(2)
print('Expected: 200')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 3: calculate_entrance_fees_1(7)")

print()

result = calculate_entrance_fees_1(7)
print('Expected: 710')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()