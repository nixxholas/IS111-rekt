with open('phone_numbers.txt') as phone_numbers_file:
    contacts = {}
    for line in phone_numbers_file:
        cols = line.rstrip().split('|')
        if cols[0] not in contacts:
            contacts[cols[0]] = [cols[1]]
        else:
            contacts[cols[0]].append(cols[1])

name = input("Enter a person’s name: ")
if name in contacts:
    print(name + ' has ' + str(len(contacts[name])) + ' number(s):')
    for n in contacts[name]:
        print('\t' + n)
else:
    print(name + ' was not found in the database.')
