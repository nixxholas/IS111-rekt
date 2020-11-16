# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
def multiply(polynomials):
    p_count = len(polynomials)  # Obtain the count of polynomials first

    while len(polynomials) > 1:
        # Always multiply the the first two polynomials first.
        first_polynomial = polynomials.pop(0)
        second_polynomial = polynomials.pop(0)

        polynomials.insert(0, multiply_polynomials(first_polynomial, second_polynomial))

    # Write your code here.
    return polynomials


def multiply_polynomials(p1, p2):
    resultant = []
    longer_polynomial = list(p1 if len(p1) > len(p2) else p2)
    shorter_polynomial = list(p1 if len(p1) < len(p2) else p2)
    if len(p1) == len(p2):
        longer_polynomial = list(p2)
        shorter_polynomial = list(p1)

    # Multiple first
    # Always compute from the back
    biggest_sp_x_power = len(shorter_polynomial) - 1
    while biggest_sp_x_power >= 0:
        # Take the sp's last coefficient to multiple
        sp_biggest_coefficient = shorter_polynomial.pop(0)

        # Seed the new polynomial inputs first.
        new_longer_polynomial = []
        for i in range(biggest_sp_x_power + len(longer_polynomial) - 1 , -1, -1):
            new_longer_polynomial.append(0)

        # Multiply all coefficients in the longer polynomial
        for i in range(len(longer_polynomial)):
            # Polynomial increment
            # coefficient_x_power = i
            current_coefficient = (len(longer_polynomial) - 1) - i
            new_coefficient_x_power = current_coefficient + biggest_sp_x_power

            target_index_in_new_polynomial = len(new_longer_polynomial) - (1 + new_coefficient_x_power)
            new_longer_polynomial[target_index_in_new_polynomial] += (longer_polynomial[i] * sp_biggest_coefficient)

        biggest_sp_x_power -= 1
        resultant.append(new_longer_polynomial)

    # Then summation
    new_polynomial = []
    for r in resultant:
        while len(r) > len(new_polynomial):
            new_polynomial.append(0)

    while len(resultant) > 1:
        first_polynomial = resultant.pop(0)
        second_polynomial = resultant.pop(0)

        smaller_polynomial = first_polynomial if len(first_polynomial) < len(second_polynomial) else second_polynomial
        bigger_polynomial = first_polynomial if len(first_polynomial) > len(second_polynomial) else second_polynomial

        # Sum from backwards
        cur_new_p_index = len(new_polynomial) - 1
        smaller_p_index = len(smaller_polynomial) - 1
        for i in range(len(bigger_polynomial) - 1, -1, -1):
            if smaller_p_index >= 0:
                new_polynomial[cur_new_p_index] += (smaller_polynomial[smaller_p_index] + bigger_polynomial[i])
                smaller_p_index -= 1
                cur_new_p_index -= 1
            else:
                new_polynomial[cur_new_p_index] += bigger_polynomial[i]

    if len(resultant) == 1:
        last_polynomial = resultant.pop(0)

        # Sum from backwards
        cur_new_p_index = len(new_polynomial) - 1
        for i in range(len(last_polynomial) - 1, -1, -1):
            new_polynomial[cur_new_p_index] += last_polynomial[i]
            cur_new_p_index -= 1

    return resultant[0] if new_polynomial == [] else new_polynomial

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