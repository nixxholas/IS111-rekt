import q2a

student_gpas = {'George Leung': 3.4, 'Eric Wong': 3.9, 'Michelle Lee': 3.1}
q2a.display_all_gpas(student_gpas)
print()
name = input('Whose GPA do you want to change? ')
if name in student_gpas:
    student_gpas[name] = float(input("What's the new GPA? "))
    print('Thanks! GPA has changed. ')
else:
    print('Sorry! This student doesn’t exist.')
print()
print('The new GPA information:')
q2a.display_all_gpas(student_gpas)