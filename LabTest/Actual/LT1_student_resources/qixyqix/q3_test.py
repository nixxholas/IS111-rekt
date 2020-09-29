from q3 import check_math

print()
print('-' * 20)
print()

print('Test Case 1: check_math([" 3 +5 =9", "4  * 3 = 12 "])')

print()

result = check_math([" 3 +5 =9", "4  * 3 = 12 "])
print('Expected: False')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: check_math(["13 % 5 = 3", "4 // 3 = 1", "90 - 50 = 40"])')

print()

result = check_math(["13 % 5 = 3", "4 // 3 = 1", "90 - 50 = 40"])
print('Expected: True')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: check_math([])')

print()

result = check_math([])
print('Expected: True')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()