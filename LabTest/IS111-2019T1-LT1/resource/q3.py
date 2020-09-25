# Name:
# Email ID:

def get_common_chars(first, second):
    return None
    
    

if __name__ == "__main__":
    print('Test 1')
    print('Expected:123')
    result = get_common_chars('abc123', '1X2Y3Z')
    print(f'Actual  :{result}')
    print()

    print('Test 2:Check data type')
    print('Expected:True')
    result = isinstance(get_common_chars('abc123', '1X2Y3Z'), str)
    print(f'Actual  :{result}')
    print()

    print('Test 3')
    print('Expected:ape')
    result = get_common_chars('apple', 'pear')
    print(f'Actual  :{result}')
    print()

    print('Test 4')
    print('Expected:buble')
    result = get_common_chars('bubble', 'rubble')
    print(f'Actual  :{result}')
    print()

    print('Test 5')
    print('Expected:be')
    result = get_common_chars('beast', 'bubble')
    print(f'Actual  :{result}')
    print()

    print('Test 6')
    print('Expected:><')
    result = get_common_chars('kiwi', 'mango')
    print(f'Actual  :>{result}<')
    print()

    print('Test 7')
    print('Expected:kingk')
    result = get_common_chars('kingkongkong', 'kiwiking')
    print(f'Actual  :{result}')
    print()


