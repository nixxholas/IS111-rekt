def check_age(student_list):
    # Modify the code below.
    for student in student_list:
        if student[1] == 'M' and int(student[2]) < 20:
            return False
    return True

