# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def compute_product(num_list):
    product = 1

    for num in num_list: 
        if num % 2 != 0:
            product *= num

    return product

