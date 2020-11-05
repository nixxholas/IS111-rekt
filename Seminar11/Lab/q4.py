## Q4 Students and Schools
# write your code below
def get_students_by_school(student_sch):
    school_students = {}

    for student in student_sch:
        # Make things clearer, define a var to stash the school
        sch = student_sch[student]
        if student_sch[student] in school_students:
            school_students[sch].append(student)
        else:
            school_students[sch] = [student]

    return school_students

