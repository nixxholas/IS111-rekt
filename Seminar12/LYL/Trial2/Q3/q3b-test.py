from q3b import add_new_email


# #####################################
# Test Cases of Q3b

address_book = {'Jack': 'jack@smu.edu.sg', 'Mary': 'mary@sis.smu.edu.sg', 'John': 'john@gmail.com'}

print()
print("Test Case 1:")

result = add_new_email(address_book, ('Jack', 'jack@gmail.com'))

print("Expected: {'Jack': 'jack@gmail.com', 'Mary': 'mary@sis.smu.edu.sg', 'John': 'john@gmail.com'}")
print("Actual  :", address_book)
print()
print("Expected: jack@smu.edu.sg")
print("Actual  :", result)

print()
print("Test Case 2:")

result = add_new_email(address_book, ('Eric', 'eric@smu.edu.sg'))

print("Expected: {'Jack': 'jack@gmail.com', 'Mary': 'mary@sis.smu.edu.sg', 'John': 'john@gmail.com', 'Eric': 'eric@smu.edu.sg'}")
print("Actual  :", address_book)
print()
print("Expected: None")
print("Actual  :", result)