def sum_up(name):
    sum = 0.0
    file = open(name, 'r')

    for line in file:
        clean_str = line.strip('\n')
        sum += float(clean_str)

    return sum


# Test cases
print('Test case 1')
print('===========')
your_sum = sum_up('q1-1.txt')
print('Expected: ', 55.4)
print('Actual:   ', round(your_sum, 1))

print('\nTest case 2')
print('===========')
your_sum = sum_up('q1-2.txt')
print('Expected: ', 55.0)
print('Actual:   ', round(your_sum, 1))
