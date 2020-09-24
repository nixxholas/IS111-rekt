from q2 import display_strings

print('Test Case 1')
print()

print('Expected output:')
print('     Spider Man-----')
print('    Iron Man-------')
print('   Hulk-----------')
print('  Thor-----------')
print(' Captain America')
print('Black Widow----')

print('Actual output  :')

my_list = ['Spider Man', 'Iron Man', 'Hulk', 'Thor', 'Captain America', 'Black Widow']
display_strings(my_list, '-')

print()

print('Test Case 2')
print()

print('Expected output:')

print('   ABC')
print('  B**')
print(' CD*')
print('D**')

print('Actual output  :')

my_list = ['ABC', 'B', 'CD', 'D']
display_strings(my_list, '*')

print()

print('Test Case 3')
print()

print('Expected output:')
print('Actual output  :')

my_list = []
display_strings(my_list, '*')

print()