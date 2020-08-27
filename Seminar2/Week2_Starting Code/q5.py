import math

#q5a
print("Each side of this square is", math.sqrt(float(input("What's the size of the square (in centimeters)? "))),
      "centimeters.")

import random

#q5b
integer = int(input("Enter a positive integer: "))
if integer <= 0:
    print("A positive integer bro")
else:
    print(random.randint(1, integer))