from q2a import get_sum_of_digits

print()
print('-' * 20)
print()

print('Test Case 1: get_sum_of_digits("1234")')

print()

result = get_sum_of_digits("1234")
print('Expected: 10')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: get_sum_of_digits("SMU1-2-3-4")')

print()

result = get_sum_of_digits("SMU1-2-3-4")
print('Expected: 10')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: get_sum_of_digits("32-4*5(0)36")')

print()

result = get_sum_of_digits("32-4*5(0)36")
print('Expected: 23')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 4: get_sum_of_digits("SMU-SIS")')

print()

result = get_sum_of_digits("SMU-SIS")
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 5: get_sum_of_digits("")')

print()

result = get_sum_of_digits("")
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()