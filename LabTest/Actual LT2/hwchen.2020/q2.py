# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
import sys

def get_hi_lo(products):
    highest = (None, -sys.maxsize)
    lowest = (None, sys.maxsize)

    if len(products) > 0 or products is not None:
        for product in products:
            if highest[1] < product[1]:
                highest = product
            if lowest[1] > product[1]:
                lowest = product

    return highest[0], lowest[0]

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    products = [('apple', 100), ('orange', 200), ('pear', 300)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('pear', 'apple')")
    print(f"Actual   : {result}")
    print()
    
    print("Expected return type : <class 'tuple'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the tuple : <class 'str'>")
    print("Actual return type of the first element of the tuple   : ", end="")
    if (isinstance(result, tuple)):
        print(type(result[0]))
    else:
        print("N/A")

    tc_num += 1
    print('-' * 40)
    
    products = [('apple',100),('orange',250),('pear',200),('banana',150)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('orange', 'apple')")
    print(f"Actual   : {result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    products = [('apple', 100)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('apple', 'apple')")
    print(f"Actual   : {result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    products = []
    print(f"Test Case {tc_num}:get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : (None, None)")
    print(f"Actual   : {result}")
    print()
