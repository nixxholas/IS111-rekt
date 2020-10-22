file = open('phone_book.txt', 'r')

users = []
user_numbers = []

for line in file:
    contact = line.rstrip().split('|')

    if len(users) == 0:
        users.append(contact[0])
        user_numbers.append([contact[1]])
    elif contact[0] in users:
        user_numbers[users.index(contact[0])].append(contact[1])
    else:
        users.append(contact[0])
        user_numbers.append([contact[1]])

output = open('phone_book_reorganized.txt', 'w')
while len(users) > 0:
    u = users.pop(0)
    u_nums = user_numbers.pop(0)

    output.write(u + '\n')
    for n in u_nums:
        output.write(n + '\n')
    output.write('\n')