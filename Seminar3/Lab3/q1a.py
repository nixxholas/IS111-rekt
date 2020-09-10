# Q1a
def perform_magic1(condition, output):
    if (condition):
        print(output)

def perform_magic2(condition, output):
    if (condition):
        print(output)
    else:
        print("The condition is false!")

def perform_magic3(a, b):
    if (a >= b):
        print("a >= b")
 
    if (a <= b):
        print("a <= b")

a = 12
b = 15

perform_magic1(a == b, "a == b")
perform_magic2(a > b, "a > b")
perform_magic3(a + 3, b)