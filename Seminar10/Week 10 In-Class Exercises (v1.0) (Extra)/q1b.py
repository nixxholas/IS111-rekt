course_term_students = {}

with open('grades.txt') as grades_file:
    for line in grades_file:
        cols = line.rstrip().split('#')
        course_and_term = (cols[1], cols[2])

        if course_and_term in course_term_students.keys():
            course_term_students[course_and_term].append(cols[0])
        else:
            course_term_students[course_and_term] = [cols[0]]

combinations = set()
for cts in course_term_students:
    if len(course_term_students[cts]) > 1:
        students = course_term_students[cts]

        # We use this to tell us which student we're spamming for combinations.
        index = 0
        while index + 1 < len(students):

            for other_student_index in range(index + 1, len(students)):
                combinations.add((students[index], students[other_student_index]))

            index += 1

print(list(combinations))
