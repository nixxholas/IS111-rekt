def display_all_gpas(student_gpa):
    print('Student Name\tStudent GPA')
    print('------------\t-----------')
    for k in student_gpa.keys():
        print(k + (' ' * (12 - len(k))) + '\t' + str(student_gpa[k]))


display_all_gpas({'George Leung': 3.4, 'Eric Wong': 3.9, 'Michelle Lee': 3.1})
