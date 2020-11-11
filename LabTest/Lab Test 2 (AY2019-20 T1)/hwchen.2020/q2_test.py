from q2 import get_longer_words

print()
print('-' * 20)
print()

print('Test Case 1: get_longer_words("q2_input_1.txt")')

print()

result = get_longer_words("q2_input_1.txt")
print("Expected: ['LKCSB', 'Python', 'return', 'float', 'a', 'IS110']")
print("Actual:   " + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: get_longer_words("q2_input_2.txt")')

print()

result = get_longer_words("q2_input_2.txt")
print("Expected: ['Grab', 'McDonald', 'Amazon', 'coffee', 'San Francisco', 'empty string']")
print("Actual:   " + str(result))

print()
print('-' * 20)
print()