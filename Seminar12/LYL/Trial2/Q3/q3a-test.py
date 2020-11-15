from q3a import retrieve_email

# #####################################
# Test Cases of Q3a

address_book = {'Jack': 'jack@smu.edu.sg', 'Mary': 'mary@sis.smu.edu.sg', 'John': 'john@gmail.com'}

# Test Case 1

print()
print("Test Case 1:")
print("Expected answer: mary@sis.smu.edu.sg")
email = retrieve_email(address_book, 'Mary')
print("Actual answer  :", email) 
print()

print("Test Case 2:")
print("Expected answer: None")
email = retrieve_email(address_book, 'Eric')
print("Actual answer  :", email)
print("Expected answer type: <class 'NoneType'>")
print("Actual answer type  :", type(email))
print()
