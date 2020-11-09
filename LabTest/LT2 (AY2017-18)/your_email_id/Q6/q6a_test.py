from q6a import scramble

print()
print("====================")
print()

file = "english_words.txt"

# Test Case 1:
print("Test Case #1:")
print()

my_list = scramble('rteid', file)
print("Expected: ['tired', 'tried']")
print("      or: ['tried', 'tired']")
print("Actual  : " + str(my_list))
print()
print("Expected type of returned value: <class 'list'>")
print("Actual type of returned value  : " + str(type(my_list)))
print()
print("====================")
print()

# Test Case 2:
print("Test Case #2:")
print()

my_list = scramble('odg', file)
print("Expected: ['dog', 'god']")
print("      or: ['god', 'dog']")
print("Actual  : " + str(my_list))
print()
print("====================")
print()

# Test Case 3:
print("Test Case #3:")
print()

my_list = scramble('ibg', file)
print("Expected: ['big']")
print("Actual  : " + str(my_list))
print()
print("====================")
print()

# Test Case 4:
print("Test Case #4:")
print()

my_list = scramble('aaaa', file)
print("Expected: []")
print("Actual  : " + str(my_list))
print()
print("====================")
print()
