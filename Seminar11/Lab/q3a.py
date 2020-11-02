facils = {}

# Load the file first
with open('facilities.txt') as facilities:
    for line in facilities:
        line = line.rstrip().split('\t')
        facils[line[0]][line[1]] = (line[2], line[3])

while input('Do you want to search for a facility? [Y|N] :'):
    sch = input('Enter the school [LKCSB|SOE|SOL|SOA|SIS] :')
    rm_no = input('Enter the room number :')
    print(line[0] + ' ' + line[1] + ' has a capacity of ' + line[2] + ' and does ' + ('' if line[3] else 'not ') + 'have a projector.')