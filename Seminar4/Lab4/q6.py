## Q6
######################################################################################
# This code is provided to you. DO NOT MODIFY THE CODE!
def calculate_price_after_discount(unit_price, quantity, discount_rate):
    """
    This function takes in the unit price, quantity and discount rate of an item.
    It returns the total price after discount for the item.
    Parameters:
        - unit_price (float): The unit price of the item.
        - quantity (int): The quantity of the item being purchased.
        - discount_rate (float): The percentage of discount. E.g., if there's a 
          10% discount, then discount_rate is set to 10.
    Return:
        - The total price of the item with the specified quantity after discount.
    """
    return unit_price * quantity * (1 - discount_rate / 100)


######################################################################################
# Write your solution below for Part A:
item_count = int(input("How many items do you want to check out? "))
items = []

for i in range(1, item_count + 1):
    print("Enter the details of Item " + str(i) + ":")
    name = input("What's this item? ")
    unit_price = float(input("'What's the unit price of this item? "))
    qty = int(input("What's the quantity of this item? "))
    has_discount = input("Does this item have any discount? [yes|no]") == "yes"
    discount = 0.0
    if has_discount: discount = float(input("What's the percentage of discount (%)? "))
    items.append((name, unit_price, qty, has_discount, discount))

total = 0.0
for i in items:
    total += (calculate_price_after_discount(i[1], i[2], i[4]) if i[3] is True else (i[1] * i[2]))

print("The total amount you have to pay is $" + str(round(total, 2)))

######################################################################################
# Write your solution below for Part B:
