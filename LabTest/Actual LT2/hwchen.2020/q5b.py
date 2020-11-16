# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
def get_polynomial(poly_str):

    # Write your code here.
    return None

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0
    
    tc_num += 1
    print('-' * 40)
    
    poly_str = '2x - 2x^2 + 3x - 1 + 6x^3'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print("Expected : [6, -2, 5, -1]")
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print() 

    print("Expected return type : <class 'list'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the list : <class 'int'>")
    print("Actual return type of the first element of the list   : ", end="")
    if (isinstance(result, list)):
        print(type(result[0]))
    else:
        print("N/A")    

    tc_num += 1
    print('-' * 40)
    
    poly_str = '  4x -2x^2 +   3x^5 -   6x^2'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print('Expected : [3, 0, 0, -8, 4, 0]')
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print()  

    tc_num += 1
    print('-' * 40)
    
    poly_str = '3x^2 - 2x - 3x^2'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print('Expected : [-2, 0]')
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print()      

