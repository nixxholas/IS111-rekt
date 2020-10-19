has_more = True
total = 0.0
cart = []

while has_more:
    has_more = input("Do you have any item left in your shopping cart? Please enter Y or N: ") == "Y"

    if has_more:
        cart.append((input("Please enter the name of the item : "),
                     float(input("Please enter the price of the item : ")),
                     int(input("Please enter the quantity of the item : "))))

print("You've entered the following items:")
for i in cart:
    total += (i[1] * i[2])
    print("\t" + i[0] + "\t$" + str(i[1]) + "\t" + str(i[2]))

print()
print("Total price: $" + str(total))
