from q4b import get_seating_arrangement

print()
print('-' * 20)
print()

print("Test Case 1: get_seating_arrangement(['Gina','Lucy','Serena'], ['Alex','Harry','Timothy'], [('Serena','Alex'),('Harry','Lucy')], [('Gina','Timothy')])")

print()
         
result = get_seating_arrangement(['Gina','Lucy','Serena'], ['Alex','Harry','Timothy'], [('Serena','Alex'),('Harry','Lucy')], [('Gina','Timothy')])


print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

expected_results = []
arrangement_1 = ['Gina', 'Harry', 'Lucy', 'Timothy', 'Serena', 'Alex']
arrangement_2 = ['Gina', 'Alex', 'Serena', 'Timothy', 'Lucy', 'Harry']

print('Expected returned arrangement starting from Gina: one of the following' )
print('\t' + str(arrangement_1))
print('\t' + str(arrangement_2))
print('Actual returned arrangment starting from Gina:')
index_of_gina = None
for index in range(len(result)):
    if result[index] == 'Gina':
        index_of_gina = index
# We shift the returned results such that we always show the
# seating arrangement starting from Gina.
print('\t' + str(result[index_of_gina:] + result[0:index_of_gina]))


print()
print('-' * 20)
print()

print("Test Case 2: get_seating_arrangement(['Gina','Lucy','Serena'], ['Alex','Harry','Timothy'], [('Gina','Alex'),('Gina','Harry'),('Harry','Lucy')], [('Timothy','Lucy')])")

print()

result = get_seating_arrangement(['Gina','Lucy','Serena'], ['Alex','Harry','Timothy'], [('Gina','Alex'),('Gina','Harry'),('Harry','Lucy')], [('Timothy','Lucy')])

print('Expected: None')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 3: ")

print()

result = get_seating_arrangement(['A', 'B', 'C', 'D'], ['a', 'b', 'c', 'd'], 
        [('A', 'a'), ('a', 'B'), ('B', 'b'), ('C','c')], 
        [])

print('Expected returned arrangement starting from A: one of the following')
arrangements = [['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd'],
        ['A', 'd', 'D', 'c', 'C', 'b', 'B', 'a'],
        ['A', 'a', 'B', 'b', 'D', 'd', 'C', 'c'],
        ['A', 'c', 'C', 'd', 'D', 'b', 'B', 'a']]
for arrangement in arrangements:
    print('\t' + str(arrangement))

print('Actual returned arrangement starting from A:')
index_of_A = None
for index in range(len(result)):
    if result[index] == 'A':
        index_of_A = index
print('\t' + str(result[index_of_A:] + result[0:index_of_A]))

print()
print('-' * 20)
print()
