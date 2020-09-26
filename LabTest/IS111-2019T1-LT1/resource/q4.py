# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

import string


def get_similarity_level(string1, string2):
    if string1 == string2: return 'same'
    if string1.lower() == string2.lower(): return 'close'
    str1nums, str1chars, str1syms, str2nums, str2chars, str2syms = 0, 0, '', 0, 0, ''
    smaller_str = list(string1 if len(string1) < len(string2) else string2)
    bigger_str = list(string1 if len(string1) > len(string2) else string2)

    for c in bigger_str:
        if c in string.ascii_letters:
            if c in smaller_str:
                smaller_str.remove(c)
                str1chars += 1
                str2chars += 1
            else:
                str2chars += 1
        elif c.isnumeric():
            if c in smaller_str:
                smaller_str.remove(c)
                str1nums += 1
                str2nums += 1
            else:
                str2nums += 1
        elif c in smaller_str:
            smaller_str.remove(c)
            str1syms += c
            str2syms += c
        else:
            str2syms += c

    if (str1nums == str2nums) and (str1chars == str2chars) and (len(string1) == len(string2)) and len(str1syms) > 0 and \
            len(str2syms) > 0:
        for c in str1syms:
            if c in str2syms:
                return 'weak'
        return 'somewhat'

    return 'different'


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
