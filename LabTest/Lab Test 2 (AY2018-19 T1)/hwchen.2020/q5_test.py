import q5

my_list = q5.convert_to_list('[4,5,[6,7],[8,[9,10]],11]')

print('Test Results:')
print()

print("Expected value:[4, 5, [6, 7], [8, [9, 10]], 11]")
print('Actual value  :' + str(my_list))
print()

print("Expected type:<class 'list'>")
print('Actual type  :' + str(type(my_list)))
print()

print('Expected length:5')
print('Actual length  :' + str(len(my_list)))
print()

print('Expected third element:[6, 7]')
if len(my_list) >= 2:
    element = my_list[2]
else:
    element = None
print('Actual third element  :' + str(element))
print()

print('Expected number:8')
if len(my_list) >= 3 and len(my_list[3]) >= 1:
    number = my_list[3][0]
else:
    number = None
print('Actual number  :' + str(number))