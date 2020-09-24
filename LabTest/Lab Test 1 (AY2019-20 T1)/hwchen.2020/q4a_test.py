from q4a import check_seating_arrangement

print()
print('-' * 20)
print()

print("Test Case 1: check_seating_arrangement(['Serena', 'Timothy', 'Lucy', 'Harry', 'Gina', 'Alex'], [('Serena', 'Alex'), ('Harry', 'Lucy')], [('Gina', 'Timothy')]")

print()

result = check_seating_arrangement(['Serena', 'Timothy', 'Lucy', 'Harry', 'Gina', 'Alex'], [('Serena', 'Alex'), ('Harry', 'Lucy')], [('Gina', 'Timothy')])

print('Expected: True')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: check_seating_arrangement(['Serena', 'Harry', 'Lucy', 'Timothy', 'Gina', 'Alex'], [('Serena', 'Alex'), ('Harry', 'Lucy')], [('Gina', 'Timothy')])")

print()

result = check_seating_arrangement(['Serena', 'Harry', 'Lucy', 'Timothy', 'Gina', 'Alex'], [('Serena', 'Alex'), ('Harry', 'Lucy')], [('Gina', 'Timothy')])

print('Expected: False')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()