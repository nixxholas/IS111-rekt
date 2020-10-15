import string

def is_valid_name(name):
    i = 0
    while i < len(name):
        if name[i] not in string.ascii_letters and name[i] != ' ':
            return False

        i += 1

    return True


while True:
    if is_valid_name(input("Enter your name: ")):
        print("Thank you!")
        break
    else:
        print("Please enter a valid name!")