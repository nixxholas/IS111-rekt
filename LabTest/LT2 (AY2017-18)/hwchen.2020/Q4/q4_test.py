from q4 import evaluate

print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()

result = evaluate("1+2-3+4")
print("Expected: 4.0")
print("Actual  : " + str(result))
print()
print("Expected type of returned value: <class 'float'>")
print("Actual type of returned value  : " + str(type(result)))
print()
print("====================")
print()

# Test Case 2:
print("Test Case #2:")
print()

result = evaluate("3.5+4*3.0/4-12/5+1.2")
print("Expected: 5.3")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:
print("Test Case #3:")
print()

result = evaluate("1.0/2")
print("Expected: 0.5")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 4:
print("Test Case #4:")
print()

result = evaluate("2")
print("Expected: 2.0")
print("Actual  : " + str(result))
print()
print("====================")
print()

