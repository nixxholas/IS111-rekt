from q4c import get_relation

family_dict = {('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter', ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}

print()
print('-' * 20)
print()

print('Test Case 1:')
print()

result = get_relation(family_dict, 'A', 'C')

print("Expected: grandfather")
print("Actual  : " + str(result))


print("Expected type of returned value: <class 'str'>")
print('Actual type of returned value  : ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2:')
print()

result = get_relation(family_dict, 'C', 'A')

print("Expected: granddaughter")
print("Actual  : " + str(result))

print()
print('-' * 20)
print()

print('Test Case 3:')
print()

result = get_relation(family_dict, 'B', 'D')

print("Expected: husband")
print("Actual  : " + str(result))

print()
print('-' * 20)
print()

print('Test Case 4:')
print()

result = get_relation(family_dict, 'D', 'A')

print("Expected: daughter-in-law")
print("Actual  : " + str(result))

print()
print('-' * 20)
print()

