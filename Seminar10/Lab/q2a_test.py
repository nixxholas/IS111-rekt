from q2a import get_universities_founded_before
# Test Cases:

my_list = get_universities_founded_before('universities-1.txt', 1905)
print("Test Case #1:")
print("Expected:", end='')
print("['University of California, Berkeley', 'Harvard University']")
print("Actual  :", end='')
print(my_list)

print("\n==========\n")

my_list = get_universities_founded_before('universities-2.txt', 1800)
print("Test Case #2:")
print("Expected:", end='')
print("['University of Cambridge', 'University of Oxford']")
print("Actual  :", end='')
print(my_list)










