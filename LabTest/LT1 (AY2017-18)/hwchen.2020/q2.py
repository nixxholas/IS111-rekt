# Name    :
# Email ID:


# start of answer
import string

def generate_digits(sentence):
    s_chars = list(sentence)
    digits_letters = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    res = ''

    while len(s_chars) > 0:
        if len(s_chars) > 0:
            c = s_chars.pop(0)

            # If compliant
            if c in string.ascii_uppercase:
                for e in digits_letters:
                    if c in e:
                        res += str(digits_letters.index(e))

    return res  # added so that this script will run. feel free to modify it
# end of answer


print('Test 1: Check if the return value is a str object')
print('Expected:True')
print('Actual  :' + str(isinstance(generate_digits('A'), str)))
print()


print('Test 2')
print('Expected:2')
print('Actual  :' + generate_digits('A'))
print()

print('Test 3')
print('Expected:79846642')
print('Actual  :' + generate_digits('PYTHONIC'))
print()



print('Test 4')
print('Expected:53354448')
print('Actual  :' + generate_digits('LEDLIGHT'))
print()
