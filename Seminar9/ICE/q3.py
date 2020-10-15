value = 0.0
while value < 100:
    value += float(input("Please pick a book. How much is it (in $)? "))
    if value < 100:
        print("You still have $" + str(value) + " left.")

print("You are done!")
print("The total price is $" + str(value))