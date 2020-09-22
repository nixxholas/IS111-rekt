# Name    : Nicholas Chen Han Wei
# Email ID: hwchen.2020@sis.smu.edu.sg

# start of answer

def print_triangle(sentence):
    # If this sentence can be printed as a triangle
    if (((len(sentence) % 3) == 0) and len(sentence) > 3) or (len(sentence) == 4):
        output = []
        curr_row = 1
        threshold = 0
        c_arr = list(sentence)

        # Populate the output first, without the gaps
        while len(c_arr) > 0:
            row = []
            if curr_row == 1:
                row.append(c_arr.pop(0))
            elif len(c_arr) > 1 and threshold + 2 < len(c_arr):
                row.append(c_arr.pop(0))
                row.append(c_arr.pop())
            else:
                while len(c_arr) > 0:
                    row.append(c_arr.pop())
            curr_row += 1
            output.append(row)
            threshold += len(row)

        space_count = len(output) - 1
        gap_count = 0
        for o in output:
            if len(o) == 1:
                print((" " * space_count) + o[0])
                gap_count += 1
            elif len(o) == 2:
                print((" " * space_count) + o[0] + (gap_count * " ") + o[1])
                gap_count += 2
            else:
                print("".join(o[::-1]))

            space_count -= 1

        return True

    return False


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