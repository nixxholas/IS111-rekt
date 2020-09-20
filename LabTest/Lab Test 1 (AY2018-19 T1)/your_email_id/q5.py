#
# Name: 
# Email ID: 
#
def expand(text):
    # write your answer between #start and #end
    #start
    return ''
    #end

print('Test 1')
print('Expected:ABC XYZ XYZ')
result = expand('ABC &5-7 XYZ')
print('Actual  :' + result)
print()

print('Test 2')
print('Expected:ABC XYZABC XYZ')
result = expand('&0-3&4-6ABC XYZ')
print('Actual  :' + result)
print()

print('Test 3')
print('Expected:C???ABC')
result = expand('&2-5ABC')
print('Actual  :' + result)
print()

print('Test 4')
print('Expected:[a b A B a b A a b A B ]')
result = expand('a b A B &0-5&0-7')
print('Actual  :[' + result + ']')
print()

print('Test 5')
print('Expected:[UVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ]')
result = expand('&20-25ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('Actual  :[' + result + ']')
print()

print('Test 6')
print('Expected:[]')
result = expand('')
print('Actual  :[' + result + ']')
print()

print('Test 7')
print('Expected:abc')
result = expand('abc')
print('Actual  :' + result)
print()