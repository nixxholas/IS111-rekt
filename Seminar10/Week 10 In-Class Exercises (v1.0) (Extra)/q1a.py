mod_students_with_a = {}

with open('grades.txt') as grades_file:
    for line in grades_file:
        cols = line.rstrip().split('#')

        if cols[3] == 'A':
            if cols[1] in mod_students_with_a.keys():
                mod_students_with_a[cols[1]].append(cols[0])
            else:
                mod_students_with_a[cols[1]] = [cols[0]]


with open('course_info.txt', 'w') as output_file:
    for mod in mod_students_with_a.keys():
        output_file.write(mod + '\n')
        for val in mod_students_with_a[mod]:
            output_file.write(val + '\n')
        output_file.write('\n')