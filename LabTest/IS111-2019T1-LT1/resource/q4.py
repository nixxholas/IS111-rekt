# Name:
# Email ID:

def get_similarity_level(string1, string2):
    return None
    

if __name__ == "__main__":       
    print('Test 1')
    print('Expected:same')
    result = get_similarity_level('hello', 'hello')
    print(f'Actual  :{result}')
    print()

    print('Test 2')
    print('Expected:same')
    result = get_similarity_level('hello#123', 'hello#123')
    print(f'Actual  :{result}')
    print()

    print('Test 3')
    print('Expected:True')
    result = isinstance(get_similarity_level('hello', 'hello'), str)
    print(f'Actual  :{result}')
    print()

    print('Test 4')
    print('Expected:close')
    result = get_similarity_level('hello', 'HelLo')
    print(f'Actual  :{result}')
    print()

    print('Test 5')
    print('Expected:close')
    result = get_similarity_level('hello123', 'HelLo123')
    print(f'Actual  :{result}')
    print()

    print('Test 6')
    print('Expected:somewhat')
    result = get_similarity_level('hello-123', 'Hello123!')
    print(f'Actual  :{result}')
    print()

    print('Test 7')
    print('Expected:somewhat')
    result = get_similarity_level('hello-123', 'HELLO123!')
    print(f'Actual  :{result}')
    print()

    print('Test 8')
    print('Expected:weak')
    result = get_similarity_level('be3', '2Me')
    print(f'Actual  :{result}')
    print()

    print('Test 9')
    print('Expected:weak')
    result = get_similarity_level('be3!', '####2Me#######')
    print(f'Actual  :{result}')
    print()

    print('Test 10')
    print('Expected:different')
    result = get_similarity_level('ape 123', 'cape123')
    print(f'Actual  :{result}')
    print()

    print('Test 11')
    print('Expected:different')
    result = get_similarity_level('bye', '2be')
    print(f'Actual  :{result}')
    print()

    print('Test 12')
    print('Expected:different')
    result = get_similarity_level('hello', 'applet')
    print(f'Actual  :{result}')
    print()