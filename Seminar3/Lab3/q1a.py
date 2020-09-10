# Q1a
def perform_magic1(condition, output):
    if (condition):  # False
        print(output)


def perform_magic2(condition, output):
    if (condition):  # False
        print(output)
    else:
        print("The condition is false!")


def perform_magic3(a, b):
    if (a >= b):  # True
        print("a >= b")

    if (a <= b): # True
        print("a <= b")


a = 12
b = 15

perform_magic1(a == b, "a == b")  # perform_magic1 won't print any output
perform_magic2(a > b, "a > b")  # prints 'The condition is false!'
perform_magic3(a + 3, b)  # Passes all conditions
