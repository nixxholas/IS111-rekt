from q1b import create_email_dict



# #####################################
# Test Cases of Q1b

# Test Case

info_list = ["Jack", "jack@gmail.com", "Mary", "mary.loh@smu.edu.sg", "John", "john.smith@microsoft.com"] 
print()
print("Test Case for Q1b:")
print("Expected answer: {'Jack': 'jack@gmail.com', 'Mary': 'mary.loh@smu.edu.sg', 'John': 'john.smith@microsoft.com'}")
print("Actual answer  :", create_email_dict(info_list))
