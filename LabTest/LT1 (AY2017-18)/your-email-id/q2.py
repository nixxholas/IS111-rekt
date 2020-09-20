# Name    :
# Email ID:


# start of answer
def generate_digits(sentence):
    return None # added so that this script will run. feel free to modify it
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
