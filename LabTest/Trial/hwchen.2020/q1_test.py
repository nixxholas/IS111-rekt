from q1 import add_first_odd_digits

print('Test Case 1')
print()
result = add_first_odd_digits(['abc123def', 'SMU2345SIS', 'XYZ0', '7777'])
print('Expected: 11')
print('Actual  : ' + str(result))

print("Expected type: <class 'int'>")
print("Actual type  : " + str(type(result)))

print()

print('Test Case 2')
print()

result = add_first_odd_digits([' 2 ', '97531', 'XYZ', ''])
print('Expected: 9')
print('Actual  : ' + str(result))

print()

print('Test Case 3')
print()

result = add_first_odd_digits([])
print('Expected: 0')
print('Actual  : ' + str(result))
