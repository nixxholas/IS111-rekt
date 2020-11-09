import q4

mrt_map = [ ['Botanic Gardens', 'Stevens', 'Newton', 'Little India', 'Rochor'], ['Newton', 'Novena', 'Toa Payoh', 'Braddell', 'Bishan'], ['Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng'] ]

print('Test 1')
print("Expected value:['Newton', 'Stevens']")
# We sort the returned list such that we do not care about
# the order the stations appear in the list.
result = sorted(q4.find_stations_within_distance(mrt_map, 'Botanic Gardens', 2))
print('Actual value  :' + str(result))
print("Expected type:<class 'list'>")
print('Actual type  :' + str(type(result)))
print()

print('Test 2')
print("Expected value:['Dhoby Ghaut', 'Farrer Park', 'Newton', 'Rochor']")
# We sort the returned list such that we do not care about
# the order the stations appear in the list.
result = sorted(q4.find_stations_within_distance(mrt_map, 'Little India', 1))
print('Actual value  :' + str(result))
print("Expected type:<class 'list'>")
print('Actual type  :' + str(type(result)))
print()

print('Test 3')
print("Expected value:['Boon Keng', 'Farrer Park', 'Little India', 'Newton', 'Novena', 'Rochor', 'Stevens']")
# We sort the returned list such that we do not care about
# the order the stations appear in the list.
result = sorted(q4.find_stations_within_distance(mrt_map, 'Dhoby Ghaut', 3))
print('Actual value  :' + str(result))
print("Expected type:<class 'list'>")
print('Actual type  :' + str(type(result)))
print()
