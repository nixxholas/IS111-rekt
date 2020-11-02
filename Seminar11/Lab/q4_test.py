from q4 import get_students_by_school

# test codes for your function 
print('\nTestcase')
print('-' * 10)
student_to_school_dict = {'Joe Tan':'SIS', 'Alan Lee':'SOE', 'George Wong':'SOSS', 'Liu Chee Hwa':'SOL', 'Ng Yew Tung':'SIS', 'Wendy Li':'SIS', 'Jerry Lim':'SOSS'}
print("Expected: ")
print("SIS :\t['Joe Tan', 'Ng Yew Tung', 'Wendy Li']")
print("SOE :\t['Alan Lee']")
print("SOSS :\t['George Wong', 'Jerry Lim']")
print("SOL :\t['Liu Chee Hwa']")
print("\nActual  : ")
school_to_student_dict = get_students_by_school(student_to_school_dict)
for key in school_to_student_dict:
    print(key + " :\t" + str(school_to_student_dict[key]))