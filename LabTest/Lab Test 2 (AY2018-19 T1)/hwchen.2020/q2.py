#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#
def get_prices_in_range(price_list, low, high):
    res = []
    for price in price_list:
        if low <= price <= high:
            res.append(price)
    return res