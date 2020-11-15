# Write your code below:
while True:
    email = input('Please enter your SMU email address:')

    if len(email.split('@')) != 2 or len(email.split('@')[0]) == 0 or len(
            email.split('@')[1]) == 0 or not email.endswith('@smu.edu.sg'):
        print('Invalid!')
    else:
        break
print('Thanks!')