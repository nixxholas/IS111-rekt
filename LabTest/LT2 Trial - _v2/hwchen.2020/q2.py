# Write your code below:
alias = '@smu.edu.sg'
email = ''
while len(email) <= len(alias) or not email.endswith(alias) or '@' in email[:len(email) - len(alias)]:
    email = input('Please enter your SMU email address:')

    if len(email) <= len(alias) or not email.endswith(alias) or '@' in email[:len(email) - len(alias)]:
        print('Invalid!')

print('Thanks!')