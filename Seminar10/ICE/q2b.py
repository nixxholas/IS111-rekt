def same_author(file_name):
    file = open(file_name, 'r')
    auth = None

    for line in file:
        if auth != line.split('\t')[1] and auth is not None:
            return False
        elif auth is None:
            auth = line.split('\t')[1]

    return True


# Test cases used to test your function
print('\nTestcase 1')
print('-' * 10)
print("Expected: False")
filename = 'books-1.txt'
result = same_author(filename)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print("Expected: True")
filename = 'books-2.txt'
result = same_author(filename)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print("Expected: False")
filename = 'books-3.txt'
result = same_author(filename)
print('Actual:   ' + str(result))
