#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020@sis.smu.edu.sg
#
def print_snake(sequence, w):
    # the “tail” of the snake is always at the bottom right corner of the output, and
    # each vertical segment of the snake has a height of 3.

    # Define the sequence as a char array in reverse.
    seq_arr = list(sequence)[::-1]
    # Define the result to print line by line in reverse.
    res_arr = []
    # Define an integer to track the vertical index, ensuring it never exceeds 2.
    ver_index = 0
    # Define a Boolean to tell us if the current vertical side must be at the left or right.
    ver_is_left = True

    # Iterate the sequence character by character
    while len(seq_arr) > 0:
        curr_line = ''

        # If we have to print horizontally
        if ver_index == 0:
            # Iterate the width
            for i in range(0, w):
                # Obtain the first element currently and take it out permanently
                if len(seq_arr) > 0:
                    curr_line += seq_arr.pop(0)
                else:
                    curr_line += ' '

            # If the vertical alignment is now to the left, we need to flip it since we're creating
            # curr_line from the left
            if ver_is_left:
                curr_line = curr_line[::-1]
        # Else we only need to print at the very end
        else:
            for i in range(0, w):
                if (ver_is_left and i == 0) or (not ver_is_left and (i == w - 1)):
                    curr_line += seq_arr.pop(0)
                else:
                    curr_line += ' '

        # If we have hit the limit
        if ver_index < 1:
            ver_index += 1
        else:
            ver_index = 0
            ver_is_left = not ver_is_left
        res_arr.append(curr_line)
        curr_line = ''  # Always reset

    while len(res_arr) > 0:
        if len(res_arr) > 0: print(res_arr.pop())


print('Test 1')
print('Expected:')
print('abcd')
print('   e')
print('ihgf')
print('j   ')
print('klmn')
print('-' * 20)
print('Actual:')
print_snake('abcdefghijklmn', 4)
print('\n')

print('Test 2')
print('Expected:')
print('cba')
print('d  ')
print('efg')
print('  h')
print('kji')
print('l  ')
print('mno')
print('-' * 20)
print('Actual:')
print_snake('abcdefghijklmno', 3)
print('\n')

print('Test 3')
print('Expected:')
print('    a')
print('fedcb')
print('g    ')
print('hijkl')
print('-' * 20)
print('Actual:')
print_snake('abcdefghijkl', 5)
print('\n')

print('Test 4')
print('Expected:')
print('   a')
print('   b')
print('fedc')
print('g   ')
print('hijk')
print('-' * 20)
print('Actual:')
print_snake('abcdefghijk', 4)
print('\n')
    
print('Test 5')
print('Expected:')
print('a   ')
print('b   ')
print('cdef')
print('-' * 20)
print('Actual:')
print_snake('abcdef', 4)
print('\n')

print('Test 6')
print('Expected:')
print('a   ')
print('bcde')
print('-' * 20)
print('Actual:')
print_snake('abcde', 4)