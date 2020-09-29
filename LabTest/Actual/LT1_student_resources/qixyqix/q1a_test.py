from q1a import get_tank_volume

print()
print('-' * 20)
print()

print('Test Case 1: get_tank_volume(30, 45, 40)')

print()

result = get_tank_volume(30, 45, 40)
print('Expected: 54')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: get_tank_volume(36, 45, 124)')

print()

result = get_tank_volume(36, 45, 124)
print('Expected: 200')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()
