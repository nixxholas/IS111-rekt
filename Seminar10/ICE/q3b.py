file = open('phone_book.txt', 'r')

users = []
user_numbers = []

for line in file:
    contact = line.rstrip().split('|')

    if len(users) == 0 or contact[0] not in users:
        users.append(contact[0])
        user_numbers.append([contact[1]])
    else:
        user_numbers[users.index(contact[0])].append(contact[1])

output = open('phone_book_reorganized.txt', 'w')
while len(users) > 0:
    u = users.pop(0)
    u_nums = user_numbers.pop(0)

    output.write(u + '\n')
    output.write("\n".join(u_nums))
    output.write('\n')
    output.write('\n')
