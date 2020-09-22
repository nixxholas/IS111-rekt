# Name    :
# Email ID:

# start of answer

def find_tags(sentence):
    s_chars = list(sentence)
    tagged_words = []

    while len(s_chars) > 0:
        c = s_chars.pop(0)

        if c == '[':
            cur_word = ''
            while s_chars[0] != ']':
                cur_word += s_chars.pop(0)
            s_chars.pop(0)
            tagged_words.append(cur_word)

    res = ''
    for i in range(0, len(tagged_words)):
        res += str(i + 1) + '-' + tagged_words[i] + ','

    return res[:-1]

# end of answer


print('Test 1')
actual = find_tags('Coding[Rocks]')
print('Expected:1-Rocks')
print('Actual  :' + actual )
print()

print('Test 2')
actual = find_tags('[apple]and[orange]and[apple]again!')
print('Expected:1-apple,2-orange,3-apple')
print('Actual  :' + actual)
print()

print('Test 3')
actual = find_tags('IAmTaking[mrt]To[SMU]ButThe[nel]IsDelayedAgain.')
print('Expected:1-mrt,2-SMU,3-nel')
print('Actual  :' + actual)
print()

print('Test 4')
actual = find_tags('')
print('Expected:><')
print('Actual  :>' +  actual + '<' )
print()

print('Test 5')
actual = find_tags('apple')
print('Expected:><')
print('Actual  :>' +  actual + '<' )
print()
