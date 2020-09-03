import retail_utility

change = 0.0
grams_purchased = 0.0
# 1kg first
kg_max_change = retail_utility.calculate_max_quantity_and_change(98.5,
                                                                 float(input("How much money do you want to spend? ")))

# Update the change
change = kg_max_change[1]

# If something is bought
if kg_max_change[0] > 0: grams_purchased += kg_max_change[0] * 1000

# If there's still spare change,
if change > 0:
    # Spend it on .5 kg
    halfkg_max_change = retail_utility.calculate_max_quantity_and_change(58.5, change)
    # Update the change as usual
    change = halfkg_max_change[1]
    # If there's any purchased, calculate it as well.
    if halfkg_max_change[0] > 0: grams_purchased += halfkg_max_change[0] * 500


print("You can buy", grams_purchased, "grams of honey. You have $" + str(change), "left as your change.")