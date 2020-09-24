from q1 import check_sum

print()
print('-' * 20)
print()

print('Test Case 1: check_sum(4, 2, 1)')

print()

result = check_sum(4, 2, 1)
print('Expected: False')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: check_sum(3, 5, 2)')

print()

result = check_sum(3, 5, 2)
print('Expected: True')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: check_sum(2, -1, 1)')

print()

result = check_sum(2, -1, 1)
print('Expected: True')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 4: check_sum(1, 0, 0)')

print()

result = check_sum(1, 0, 0)
print('Expected: False')
print('Actual:   ' + str(result))


print()
print('-' * 20)
print()

print('Test Case 5: check_sum(-1, 0, -1)')

print()

result = check_sum(-1, 0, -1)
print('Expected: True')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()