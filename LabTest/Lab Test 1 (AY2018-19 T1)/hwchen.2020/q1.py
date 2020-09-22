#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#
def get_color(code):
    # write your answer between #start and #end
    return 'Red' if (code == 'R' or code == 'r') else 'Green' if (code == 'G' or code == 'g') else 'Blue' \
        if (code == 'B' or code == 'b') else 'Invalid'


print('Test 1')
print('Expected:Red')
result = get_color('R')
print('Actual  :' + result)
print()

print('Test 2')
print('Expected:Green')
result = get_color('g')
print('Actual  :' + result)
print()

print('Test 3')
print('Expected:Blue')
result = get_color('B')
print('Actual  :' + result)
print()

print('Test 4')
print('Expected:Invalid')
result = get_color('big')
print('Actual  :' + result)
print()

print('Test 5')
print('Expected:Invalid')
result = get_color('x')
print('Actual  :' + result)
