import q1

# #####################################
# Test Cases of Q1

# Test Case 1
temperature_list = [36.9, 36.6, 37.8, 36.7, 38.0, 37.2]

print("Test Cases for Q1")
print()
print("Test Case 1:")
print("Expected answer: 2")
print("Actual answer  :", q1.count_high_temperatures(temperature_list))
print()

# Test Case 2
temperature_list = []

print("Test Case 2:")
print("Expected answer: 0")
print("Actual answer  :", q1.count_high_temperatures(temperature_list))
print()

# Test Case 3
temperature_list = [37.5, 37.8, 36.5, 37.0]

print("Test Case 3:")
print("Expected answer: 1")
print("Actual answer  :", q1.count_high_temperatures(temperature_list))
print()