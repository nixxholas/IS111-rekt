from q1 import compute_product

print()
print('-' * 20)
print()

print('Test Case 1: compute_product([1, 2, 3, 4])')

print()

result = compute_product([1, 2, 3, 4])
print('Expected: 3')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: compute_product([1, 3, 5])')

print()

result = compute_product([1, 3, 5])
print('Expected: 15')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: compute_product([2, 4, 6, 8, 111])')

print()

result = compute_product([2, 4, 6, 8, 111])
print('Expected: 111')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 4: compute_product([-2, -3, -5, -3, 100])')

print()

result = compute_product([-2, -3, -5, -3, 100])
print('Expected: -45')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 5: compute_product([4, 40, 400])')

print()

result = compute_product([4, 40, 400])
print('Expected: 1')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 6: compute_product([])')

print()

result = compute_product([])
print('Expected: 1')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()