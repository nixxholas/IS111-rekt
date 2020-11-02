from q5a import count_words_in_file

file = 'spam_sms.txt'
my_dict = count_words_in_file(file)

print('\nTestcase 1')
print('-' * 10)
print("Expected: 204")
print("Actual  : " + str(my_dict['the']))

print('\nTestcase 2')
print('-' * 10)
print("Expected: 58")
print("Actual  : " + str(my_dict['prize']))

print('\nTestcase 3')
print('-' * 10)
print("Expected: 1")
print("Actual  : " + str(my_dict['presleys']))
