# Name:
# Email ID:
def multiply(polynomials):

    # Write your code here.
    return None

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0
    
    tc_num += 1
    print('-' * 40)
    
    polynomials = [(1, 2, 3), (5, 6, 7)]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print("Expected : [5, 16, 34, 32, 21]")
    result = multiply(polynomials)
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
    
    polynomials = [[1, 2], [3, 4, 5], [6, 7, 8]]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print('Expected : [18, 81, 172, 231, 174, 80]')
    print(f"Actual   : {multiply(polynomials)}")
    print() 
    
    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 2], [0], [3, 4, 5], [6, 7, 8]]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print('Expected : [0]')
    print(f"Actual   : {multiply(polynomials)}")
    print()     

    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 2, 3], [5, 6, 7], [8, 9, 0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [40, 173, 416, 562, 456, 189, 0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()    

    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 1, -1, 1], [2, 0], [8, 9, 0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [16, 34, 2, -2, 18, 0, 0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()    

    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1], [0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()    

    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 5, 0, 4]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print(f'multiply({polynomials})')
    print('Expected : [1, 5, 0, 4]')
    print(f'Actual   : {multiply(polynomials)}')
    print()    