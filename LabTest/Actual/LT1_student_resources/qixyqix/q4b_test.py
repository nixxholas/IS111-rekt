from q4b import trace_contacts_2

print()
print('-' * 20)
print()

print('Test Case 1:')

print()

history = [("Jason", "Gideon", -3), 
           ("Zac", "Yacob", -3),
           ("Gideon", "Brian", -1), 
           ("Cindy", "Gideon", -2), 
           ("Darren", "Jason", -5), 
           ("Jason", "Vivian", -6)]

result = trace_contacts_2("Jason", history, 5, 7)

print("Expected: ['Gideon', 'Darren', 'Brian'] (or any permutation of these three people)")
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 2:')

history = [("B", "A", -5),
           ("C", "A", -1), 
           ("B", "C", -2)]

result = trace_contacts_2("A", history, 5, 7)

print("Expected: ['B', 'C'] (or any permutation of these two people)")
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3:')

history = [("X", "A", -6),
           ("Y", "A", -6),
           ("B", "A", -5),
           ("A", "C", -5),
           ("Z", "X", -4),
           ("A", "X", -4),
           ("C", "D", -3),
           ("E", "D", -2), 
           ("D", "F", -1)]

result = trace_contacts_2("A", history, 5, 7)

print("Expected: ['B', 'C', 'X', 'D', 'F'] (or any permutation of these five people)")
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 4:')

history = [("X", "A", -6),
           ("Y", "A", -6),
           ("B", "A", -5),
           ("A", "C", -5),
           ("Z", "X", -4),
           ("A", "X", -4),
           ("C", "D", -3),
           ("Z", "U", -3),
           ("E", "D", -2),
           ("U", "V", -2),           
           ("D", "F", -1)]

result = trace_contacts_2("A", history, 6, 7)

print("Expected: ['X', 'Y', 'B', 'C', 'Z', 'D', 'U', 'E', 'F', 'V'] (or any permutation of these ten people)")
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()