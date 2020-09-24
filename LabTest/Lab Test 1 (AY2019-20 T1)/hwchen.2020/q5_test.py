from q5 import transform

def differ_by_one(str1, str2):
    diff_index_list = []
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            diff_index_list.append(i)
    if len(diff_index_list) == 2 and diff_index_list[1] == diff_index_list[0] + 1 and str1[diff_index_list[0]] == str2[diff_index_list[1]] and str1[diff_index_list[1]] == str2[diff_index_list[0]]:
        return True
    else:
        return False

def check_correctness(result, str1, str2):

    if result == [] or result[0] != str1 or result[len(result) - 1] != str2:
        print('Incorrect!')
    else:
        all_differ_by_one = True
        for index in range(0, len(result) - 1):
            if not differ_by_one(result[index], result[index+1]):
                all_differ_by_one = False
        if (all_differ_by_one):
            print('Correct!')
        else:
            print('Incorrect!')
    

print()
print('-' * 20)
print()

print("Test Case 1: transform('ABC', 'CBA')")

print()

str1 = 'ABC'
str2 = 'CBA'
result = transform(str1, str2)

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

print('Your returned sequence: ' + str(result))

check_correctness(result, str1, str2)

print()
print('-' * 20)
print()

print("Test Case 2: transform('ABCDE', 'DBECA')")

print()

str1 = 'ABCDE'
str2 = 'DBECA'
result = transform(str1, str2)

print('Your returned sequence: ' + str(result))

check_correctness(result, str1, str2)

print()
print('-' * 20)
print()