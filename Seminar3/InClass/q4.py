def get_discount_rate(num_boxes):
    return 0.2 if num_boxes >= 5 else 0.1 if num_boxes >= 2 else 0


def calculate_total_amount(brand, num_boxes):
    # Returns the total amount the customer
    # has to pay for buying that number of boxes of mooncakes of that brand
    discount = get_discount_rate(num_boxes)

    if brand == 'Tung Lok':
        return 55.4 * num_boxes if discount <= 0 else (55.4 * num_boxes) * (1 - discount)
    elif brand == 'Man Fu Yuan':
        return 59.6 * num_boxes if discount <= 0 else (59.6 * num_boxes) * (1 - discount)
    else:
        return -1


print("You need to pay $" + str(calculate_total_amount(input("Which brand do you want to buy? "),
                                                       int(input("How many boxes do you want to buy? ")))))
