facils = {}

# Load the file first
with open('facilities.txt') as facilities:
    for line in facilities:
        line = line.rstrip().split('\t')
        facils[line[0], line[1]] = (line[2], line[3])

while input('Do you want to search for a facility? [Y|N] :') == 'Y':
    room = (input('Enter the school [LKCSB|SOE|SOL|SOA|SIS] :'), input('Enter the room number :'))

    if room in facils:
        line = facils[room]
        print(room[0] + ' ' + room[1] + ' has a capacity of ' + line[0] + ' and does ' + ('' if line[1] else 'not ')
              + 'have a projector.')
    else:
        print('The specific room details were not found.')
    print()

