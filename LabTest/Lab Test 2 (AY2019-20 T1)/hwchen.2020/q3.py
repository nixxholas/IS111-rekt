# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def compute_total_price(price_dict, item_list):
    # Modify the code below.
    total = 0.0

    for item in item_list:
        item_name = item[0]
        item_qty = item[1]

        if item_name in price_dict.keys() and item_qty > 0:
            total += (price_dict[item_name] * float(item_qty))

    return total

