# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def conditional_sum(start, end, multiple):
    res_flow = ''
    res = 0

    if multiple < end:
        for i in range(start, end + 1):
            if i % multiple == 0:
                res_flow += (str(i) + ' + ')
                res += i

        return res_flow[:-2] + '= ' + str(res)

    return ''
     

if __name__ == "__main__":
    print('Test 1')
    result = conditional_sum(1, 10, 3)
    print('Expected:3 + 6 + 9 = 18')
    print(f'Actual  :{result}')
    print()

    print('Test 2: Check data type')
    result = isinstance(conditional_sum(1, 10, 3), str)
    print('Expected:True')
    print(f'Actual  :{result}')
    print()

    print('Test 3')
    result = conditional_sum(3, 12, 3)
    print('Expected:3 + 6 + 9 + 12 = 30')
    print(f'Actual  :{result}')
    print()

    print('Test 4')
    result = conditional_sum(1, 10, 11)
    print('Expected:><')
    print(f'Actual  :>{result}<')
    print()

    print('Test 5')
    result = conditional_sum(2, 22, 11)
    print('Expected:11 + 22 = 33')
    print(f'Actual  :{result}')
    print()

    print('Test 6')
    result = conditional_sum(-5, 22, 3)
    print('Expected:-3 + 0 + 3 + 6 + 9 + 12 + 15 + 18 + 21 = 81')
    print(f'Actual  :{result}')
    print()