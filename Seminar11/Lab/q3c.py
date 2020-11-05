facils = {}

# Load the file first
with open('facilities.txt') as facilities:
    for line in facilities:
        line = line.rstrip().split('\t')
        if line[0] not in facils:
            facils[line[0]] = [(line[1], line[2], line[3])]
        else:
            facils[line[0]].append((line[1], line[2], line[3]))

while input('Do you want to search for the facilities within a school? [Y|N] :') == 'Y':
    school = input('Enter the school [LKCSB|SOE|SOL|SOA|SIS] :')
    min_cap = int(input('Enter the minimum capacity you need:'))

    if school in facils:
        print('The following facilities with a capacity of ' + str(min_cap) + ' or above are found in ' + school + ':')
        print('\tRoom #\tCap\tProjector?')
        print('\t------\t---\t----------')
        rooms = [i for i in facils[school] if int(i[1]) >= min_cap]
        if len(rooms) > 0:
            for room in rooms:
                print('\t' + room[0] + '\t' + room[1] + '\t' + room[2])
        else:
            print('There are no rooms in ' + school + '.')
    else:
        print('The specified school was not found.')
    print()

print('Thanks for using our system!')
