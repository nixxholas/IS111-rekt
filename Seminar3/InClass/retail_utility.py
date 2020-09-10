def calculate_max_quantity_and_change(unit_price, amount):
    return int(amount // unit_price), amount - ((amount // unit_price) * unit_price)

# print(calculate_max_quantity_and_change(58.5, 130.0))
