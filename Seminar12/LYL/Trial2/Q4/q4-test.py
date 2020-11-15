from q4 import process_numbers

def read_from_file (file):
    result = []
    with open(file) as file:
        for line in file:
            result.append(line.rstrip())

    return result

def compare_files(file1, file2):
    content1 = read_from_file(file1)
    content2 = read_from_file(file2)

    if len(content1) != len(content2):
        return False

    for i in range(len(content1)):
        if content1[i] != content2[i]:
            return False

    return True

print ('Test 1: "normal" file')
process_numbers("numbers1.txt", "output1.txt")
print ('Expected:True')
result = compare_files('output1.txt', 'expected1.txt')
print ('Actual  :' + str(result))
print()

print ('Test 2: 1 empty line')
process_numbers("numbers2.txt", "output2.txt")
print ('Expected:True')
result = compare_files('output2.txt', 'expected2.txt')
print ('Actual  :' + str(result))
print()

print ('Test 3: 1 empty value')
process_numbers("numbers3.txt", "output3.txt")
print ('Expected:True')
result = compare_files('output3.txt', 'expected3.txt')
print ('Actual  :' + str(result))
print()

print ('Test 4: empty file')
process_numbers("numbers4.txt", "output4.txt")
print ('Expected:True')
result = compare_files('output4.txt', 'expected4.txt')
print ('Actual  :' + str(result))
print()