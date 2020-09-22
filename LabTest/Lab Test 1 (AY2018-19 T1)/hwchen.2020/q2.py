#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#
def represent_numbers(start, end):
    # write your answer between #startcode and #endcode
    res = ''

    for n in range(start, end + 1):
        res += ("-" * abs(n)) + "#"

    return res[:-1]


print('Test 1')
print('Expected:-#--#---#----#-----')
print('Actual  :' + represent_numbers(1, 5))
print()

print('Test 2')
print('Expected:---#----#-----')
print('Actual  :' + represent_numbers(3, 5))
print()

print('Test 3')
print('Expected:-')
print('Actual  :' + represent_numbers(1, 1))
print()

print('Test 4')
print('Expected:[]')
print('Actual  :[' + represent_numbers(4, 1) + ']')
print()

print('Test 5')
print('Expected:----#---#--#-##-')
print('Actual  :' + represent_numbers(-4, 1))
print()
