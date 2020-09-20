#
# Name: 
# Email ID: 
#
def print_dancing_string(sentence, start):
    # write your answer between #start and #end
    #start
    print()
    #end


print('Test 1')
print('Expected:')
print('| |')
print('|a|')
print('| |')
print('-' * 20)
print('Actual:')
print_dancing_string('a', 'M') 
print()

print('Test 2')
print('Expected:')
print('| b|')
print('|a |')
print('|  |')
print('-' * 20)
print('Actual:')
print_dancing_string('ab', 'M') 
print()

print('Test 3')
print('Expected:')
print('| b |')
print('|a c|')
print('|   |')
print('-' * 20)
print('Actual:')
print_dancing_string('abc', 'M') 
print()

print('Test 4')
print('Expected:')
print('| b  |')
print('|a c |')
print('|   d|')
print('-' * 20)
print('Actual:')
print_dancing_string('abcd', 'M') 
print()

print('Test 5')
print('Expected:')
print('| b   f   |')
print('|a c e g i|')
print('|   d   h |')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'M')
print()

print('Test 6')
print('Expected:')
print('|a   e   i|')
print('| b d f h |')
print('|  c   g  |')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'T')
print()

print('Test 7')
print('Expected:')
print('|  c   g  |')
print('| b d f h |')
print('|a   e   i|')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'B')
print()

print('Test 8')
print('Expected:')
print('||')
print('||')
print('||')
print('-' * 20)
print('Actual:')
print_dancing_string('', 'T') 
print()


