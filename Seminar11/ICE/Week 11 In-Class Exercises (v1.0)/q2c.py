import q2a

student_gpas = {'George Leung': 3.4, 'Eric Wong': 3.9, 'Michelle Lee': 3.1}
q2a.display_all_gpas(student_gpas)
print()
while True:
    name = input('Whose GPA do you want to add? ')
    if name not in student_gpas:
        student_gpas[name] = float(input("What's the GPA of " + name))
        print('Thanks! GPA has been added.\n')
        print('The new GPA information:')
        q2a.display_all_gpas(student_gpas)
        break
    else:
        print('Sorry! This student already exists.')
        print()