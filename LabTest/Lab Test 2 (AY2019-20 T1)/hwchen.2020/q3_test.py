from q3 import compute_total_price

print()
print('-' * 20)
print()

print('Test Case 1:')

price_dict = {"keyboard": 25.5, "mouse": 10.6}
item_list = [("keyboard", 1), ("mouse", 3)]

result = compute_total_price(price_dict, item_list)

print("Expected: 57.3")
print("Actual:   " + str(result))

print("Expected type of returned value: <class 'float'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2:')

price_dict = {"A": 2.5, "B": 4.0, "C": 9.0}
item_list = [("A", 2), ("C", 10)]

result = compute_total_price(price_dict, item_list)

print("Expected: 95.0")
print("Actual:   " + str(result))

print()
print('-' * 20)
print()

print('Test Case 3:')

price_dict = {"a": 1.0, "b": 2.0, "c": 3.0}
item_list = [("a", 0), ("b", 1), ("c", 2), ("b", 2)]

result = compute_total_price(price_dict, item_list)

print("Expected: 12.0")
print("Actual:   " + str(result))

print()
print('-' * 20)
print()

print('Test Case 4:')

price_dict = {"a": 1.0, "b": 2.0}
item_list = [("b", 1), ("c", 2)]

result = compute_total_price(price_dict, item_list)

print("Expected: 2.0")
print("Actual:   " + str(result))

print()
print('-' * 20)
print()

print('Test Case 5:')

price_dict = {"a": 1.0, "b": 2.0}
item_list = []

result = compute_total_price(price_dict, item_list)

print("Expected: 0.0")
print("Actual:   " + str(result))

print()
print('-' * 20)
print()
