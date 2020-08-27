import random

#q5b
integer = int(input("Enter a positive integer: "))
if integer <= 0:
    print("A positive integer bro")
else:
    print(random.randint(1, integer))