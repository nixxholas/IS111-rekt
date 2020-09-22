# Name    : Nicholas Chen Han Wei
# Email ID: hwchen.2020@sis.smu.edu.sg

# start of answer
def get_longest_word(first, second, third):
    return first if (len(first) > len(second) and len(first) > len(third)) else second if (
            len(second) > len(first) and len(second) > len(third)) else third if (
            len(third) > len(second) and len(third) > len(first)) else None

# end of answer

print('Test 1')
print('Expected:abc')
result = get_longest_word ('', 'a', 'abc')
print('Actual  :' + result)
print()

print('Test 2')
print('Expected:abcd')
result = get_longest_word ('abcd', 'a', 'ab')
print('Actual  :' + result)
print()

print('Test 3')
print('Expected:strawberry')
result = get_longest_word ('orange', 'strawberry', 'x')
print('Actual  :' + result)
