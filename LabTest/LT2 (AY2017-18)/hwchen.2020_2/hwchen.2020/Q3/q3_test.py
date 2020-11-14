from q3 import get_postal_codes

print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
my_file = "addresses-1.txt"
my_list = get_postal_codes(my_file)
print("Expected: [('Jason Wong', '560444'), ('Ted Ng', '520704'), ('Lindy Tan', '600310')]")
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
my_file = "addresses-2.txt"
my_list = get_postal_codes(my_file)
print("Expected: [('Jack', '100000'), ('Mary', '200000'), ('Joe', '300000'), ('Lincoln', '432100')]")
print("Actual  : " + str(my_list))
print()
print("====================")
print()