pin1, pin2 = '', ''
while pin1 == '':
    pin1 = input("Enter your new PIN: ")
    pin2 = input("Confirm your new PIN: ")
    if len(pin1) == 6 and pin1.isnumeric() and pin1 == pin2:
        print("Thanks! Your new PIN has been set!")
    else:
        print("Sorry! The following errors are detected:")

        if len(pin1) > 6:
            print('    - The PIN number is too long.')
        elif len(pin1) < 6:
            print('    - The PIN number is too short.')
        if not pin1.isnumeric():
            print('    - The PIN number contains a non-digit character.')
        if pin1 != pin2:
            print('    - The second PIN doesn\'t match the first PIN.')

        pin1 = ''
