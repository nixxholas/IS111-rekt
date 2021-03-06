# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def repeat(word, n):
    return '' if len(word) < 1 else word[0] * n + repeat(word[1:len(word)], n)
    

if __name__ == "__main__":
    print('Test 1')
    result = repeat('Hello!', 3)
    print('Expected:HHHeeellllllooo!!!')
    print(f'Actual  :{result}')
    print()

    print('Test 2:Check data Type')
    result = isinstance(repeat('Hello!', 3), str)
    print('Expected:True')
    print(f'Actual  :{result}')
    print()

    print('Test 3')
    result = repeat('apple', 0)
    print('Expected:><')
    print(f'Actual  :>{result}<')
    print()

    print('Test 4')
    result = repeat('', 3)
    print('Expected:><')
    print(f'Actual  :>{result}<')
    print()
