## Q2 PART 1
# These variables are defined for you to use.
MEMBER_DISCOUNT_RATE = 0.10
SALE_ITEM_DISCOUNT_RATE = 0.05


# This function is for you to implement!
def calculate_price(orig_price, is_member, is_on_sale):
    # ################################################################################
    # Modify the code below to return the correct discounted price.
    discount = 0
    if is_member: discount += MEMBER_DISCOUNT_RATE
    if is_on_sale: discount += SALE_ITEM_DISCOUNT_RATE

    return orig_price - (orig_price * discount)
    # ################################################################################


## Q2 PART 2
# Write your code below to prompt the user for the following information: 
# (1) The original price of the item. 
# (2) Whether the user is a member or not. 
# (3) Whether the item is on sale or not.:
print("The final price of the item is $" + str(calculate_price(float(input("Enter the original price of the item: ")),
                bool(input("Are you a member? (Yes or leave empty if no) ")),
                bool(input("Is the item on sale? (Yes or leave empty if no) ")))))
