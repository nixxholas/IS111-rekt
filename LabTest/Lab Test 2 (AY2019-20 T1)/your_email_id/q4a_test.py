from q4a import store_family_relations

print()
print('-' * 60)
print()

print('Test Case 1:')
print()

expected = {('A', 'C'):'father', ('C', 'A'):'daughter', ('B', 'C'):'mother', ('C', 'B'):'daughter'}

result = store_family_relations('family_file_1.txt')

print("Expected: " + str(expected))
print()
print("Actual  : " + str(result))
print()

print("Is the returned dictionary the same as expected? " + str(expected == result))

print() 

print("Expected type of returned value: <class 'dict'>")
print('Actual type of returned value  : ' + str(type(result)))

print()
print('-' * 60)
print()

print('Test Case 2:')
print()

expected = {('Adam', 'Cindy') : 'father', ('Adam', 'Darren') : 'father', ('Bella', 'Cindy') : 'mother', ('Bella', 'Darren') : 'mother', ('Cindy', 'Adam') : 'daughter', ('Cindy', 'Bella') : 'daughter', ('Darren', 'Adam') : 'son', ('Darren', 'Bella') : 'son', ('Eric', 'George') : 'father', ('Fiona', 'George'):'mother', ('George', 'Eric'):'son', ('George', 'Fiona'):'son'}

result = store_family_relations('family_file_2.txt')

print("Expected: " + str(expected))
print()
print("Actual  : " + str(result))
print()

print("Is the returned dictionary the same as expected? " + str(expected == result))

print()
print('-' * 60)
print()

print('Test Case 3:')
print()

expected = {('Jason', 'Jerry'): 'father', ('Fenny', 'Jerry'): 'mother', ('Jason', 'Jeremy'): 'father', ('Fenny', 'Jeremy'): 'mother', ('Jason', 'Jenny'): 'father', ('Fenny', 'Jenny'): 'mother', ('Jerry', 'Jason'): 'son', ('Jerry', 'Fenny'): 'son', ('Jeremy', 'Jason'): 'son', ('Jeremy', 'Fenny'): 'son', ('Jenny', 'Jason'): 'daughter', ('Jenny', 'Fenny'): 'daughter', ('Jemery', 'George'): 'father', ('Cindy', 'George'): 'mother', ('George', 'Jemery'): 'son', ('George', 'Cindy'): 'son', ('Jenny', 'Wendy'): 'father', ('Henry', 'Wendy'): 'mother', ('Jenny', 'Mike'): 'father', ('Henry', 'Mike'): 'mother', ('Wendy', 'Jenny'): 'daughter', ('Wendy', 'Henry'): 'daughter', ('Mike', 'Jenny'): 'son', ('Mike', 'Henry'): 'son'}

result = store_family_relations('family_file_3.txt')

print("Expected: " + str(expected))
print()
print("Actual  : " + str(result))
print()

print("Is the returned dictionary the same as expected? " + str(expected == result))

print()
print('-' * 60)
print()