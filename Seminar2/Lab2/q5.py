# Lab2_Q5
# ########################################
# # lab2_Q5_part1: Write your code below:
def calculate_price_after_discount(unit_price, quantity, discount):
    """
    unit_price: The unit price of an item
    quantity: The quantity of that item
    discount: The discount rate offered by the store for that item

    returns: The discount rate offered by the store for that item
    """
    return unit_price * quantity * (1 - discount / 100)


# ########################################
# lab2_Q5_part2: Write your code below:

total = 0.0
total = total + calculate_price_after_discount(5.95, 2, 10) + calculate_price_after_discount(6.50, 1, 5) \
        + calculate_price_after_discount(2.4, 2, 0) + calculate_price_after_discount(3.95, 3, 15)
print("The total of your shopping cart after discount is $" + str(total))
# print("Ruler:", calculate_price_after_discount(1.5, 5, 10))
# print("Milk:", calculate_price_after_discount(5.95, 2, 10))
# print("Rice:", calculate_price_after_discount(6.50, 1, 5))
# print("Eggs:", calculate_price_after_discount(2.4, 2, 0))
# print("Kaya:", calculate_price_after_discount(3.95, 3, 15))
