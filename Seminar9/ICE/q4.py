pin1 = ''
while pin1 == '':
    pin1 = input("Enter your new PIN: ")
    if len(pin1) == 6 and pin1.isnumeric() and pin1 == input("Confirm your new PIN: "):
        print("Thanks! Your new PIN has been set!")
    else:
        print("Sorry! There is an error!")
        pin1 = ''
