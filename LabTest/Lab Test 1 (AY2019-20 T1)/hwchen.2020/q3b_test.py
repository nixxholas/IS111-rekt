from q3b import calculate_entrance_fees_2

print()
print('-' * 20)
print()

print("Test Case 1: calculate_entrance_fees_2(2, 1)")

print()

result = calculate_entrance_fees_2(2, 1)
print('Expected: 185')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: calculate_entrance_fees_2(5, 7)")

print()

result = calculate_entrance_fees_2(5, 7)
print('Expected: 610')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 3: calculate_entrance_fees_2(3, 0)")

print()

result = calculate_entrance_fees_2(3, 0)
print('Expected: 215')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()