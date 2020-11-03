employees = {}

with open('employees.txt') as file:
    for line in file:
        cols = line.rstrip().split('\t')
        id = int(cols.pop(0).split(':')[1])

        employee_details = {}
        for i in range(len(cols)):
            columns = cols[i].split(':')

            employee_details[columns[0]] = int(columns[1]) if columns[1].isnumeric() else columns[1]

        employees[id] = employee_details

id = -1
while id == -1 or input('Do you want to search for another employee? [Y|N]:') == 'Y':
    id = int(input('Enter an employee ID: '))
    if id in employees:
        employee = employees[id]

        print('This employee is ' + employee['name'] + '.')
        field = ''
        while field != 'S':
            field = input("\tEnter a field name or 'S' to stop: ")

            if field in employee:
                print('\tThe ' + field + ' is ' + str(employee[field]))
            elif field != 'S':
                print('\tNot found!')
    else:
        print('Not found!')
    print()
