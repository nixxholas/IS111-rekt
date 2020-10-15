while True:
    if 101 > int(input("Enter your age (between 0 and 100, both inclusive): ")) >= 0:
        print("Thanks!")
        break
    else:
        print("Please enter a valid age!")


def cuter_while(value):
    value = int(input("Enter your age (between 0 and 100, both inclusive): "))

    if -1 < value < 101:
        print("Thanks!")

    return cuter_while(value) if (value > 100) or (value < 0) else value
