file = open('phone_book.txt', 'r')

for line in file:
    contact = line.rstrip().split('|')

    if ('(+65)' in contact[1][0:5]) or ('+65 ' in contact[1][0:4]) or (len(contact[1]) == 8 and contact[1].isnumeric()):
        print(contact[0] + '\t' + contact[1])
