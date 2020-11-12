import q4

########## TEST CASE 1 ##########
print()
print('-' * 20)
print()
print('Test 1')
print('Expected:', ('D2', 'D4', 3), 'or', ('D4', 'D2', 3))
result = q4.get_document_pair('documents.txt')
print('Actual:  ', result)
print()
