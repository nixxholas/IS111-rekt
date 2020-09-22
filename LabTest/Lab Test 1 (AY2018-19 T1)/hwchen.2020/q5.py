#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#
def expand(text):
    # write your answer between #start and #end
    indexer = []  # Stores the characters in 'index-reference'
    result = []  # The resultant string but in array format. Hi Nic => [ 'H', 'i', ' ', ...]

    t_arr = list(text)  # Define the text var as an array/list.
    # Build the indexer first.
    while len(t_arr) > 0:
        # POP the first character in t_arr.
        c = t_arr.pop(0)

        # If the current character is equal to ampersand (&), it means that we have found an index-reference.
        if c == '&':
            # Since we've found an index reference, we obtain the range as well.
            # ALSO account for numbers more than a digit. 5-7, 20-25
            while len(t_arr) > 0 and (t_arr[0].isnumeric() or t_arr[0] == '-'):
                t_arr.pop(0)
        else:
            indexer.append(c)

    text_chars = list(text)
    # Build the result.
    while len(text_chars) > 0:
        c = text_chars.pop(0)

        if c != '&':
            result.append(c)
        else:
            # Settle the start var
            start = ''
            while text_chars[0].isnumeric():
                start += text_chars.pop(0)
            start = int(start)

            # Take out the '-'
            t = text_chars.pop(0)
            if t != '-':
                print("Something is wrong! - does not exist between index reference range!")
                exit()

            end = ''
            while len(text_chars) > 0 and text_chars[0].isnumeric():
                end += text_chars.pop(0)
            end = int(end)

            for i in range(start, end + 1):
                result.append(indexer[i] if i < len(indexer) else '?')

    return "".join(result)


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