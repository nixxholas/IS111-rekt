# Name:
# Email ID:

def transform(source, destination):
    return None



if __name__ == "__main__":       
    print('Test 1')
    result = transform('ABC', 'CAB')
    print('Expected:ABC-ACB-CAB')
    print(f'Actual  :{result}')
    print()

    print('Test 2:Check data type')
    result = isinstance(transform('ABC', 'CAB'), str)
    print('Expected:True')
    print(f'Actual  :{result}')
    print()

    print('Test 3')
    result = transform('ABCD', 'DCAB')
    print('Expected:ABCD-ACBD-ACDB-CADB-CDAB-DCAB')
    print(f'Actual  :{result}')
    print()

    print('Test 4')
    result = transform('ABCDE', 'DBECA')
    print('Expected:ABCDE-BACDE-BCADE-BCDAE-BCDEA-BDCEA-BDECA-DBECA')
    print(f'Actual  :{result}')
    print()