# Name    :
# Email ID:

# start of answer

def print_triangle(sentence):
    return None # added so that this script will run. feel free to modify it


# end of answer


print('Test 1')
print('Expected output:')
print('   a')
print('  b l')
print(' c   k')
print('defghij')
print('Expected return value:True')
print('Actual output:')
result = print_triangle('abcdefghijkl')
print('Actual return value  :' + str(result))
print()

print('Test 2')
print('Expected output:')
print('         A')
print('        B 9')
print('       C   8')
print('      D     7')
print('     E       6')
print('    F         5')
print('   G           4')
print('  H             3')
print(' I               2')
print('JKLMNOPQRSTUVWXYZ01')
print('Expected return value:True')
print('Actual output:')
result = print_triangle('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print('Actual return value  :' + str(result))
print()

print('Test 3')
print('Expected output:')
print('Expected return value:False')
print('Actual output:')
result = print_triangle('abcdefghij')
print('Actual return value  :' + str(result))
print()

print('Test 4')
print('Expected output:')
print('Expected return value:False')
print('Actual output:')
result = print_triangle('abc')
print('Actual return value  :' + str(result))
print()

print('Test 5')
print('Expected output:')
print(' a')
print('bcd')
print('Expected return value:True')
print('Actual output:')
result = print_triangle('abcd')
print('Actual return value  :' + str(result))
print()