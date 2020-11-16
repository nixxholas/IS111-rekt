# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
def calculate_term_gpa(term_grades, mapping):
    grades = []
    points = 0

    # Convert first
    current_grade = ''
    for c in term_grades:
        if current_grade == '':
            current_grade += c
        elif current_grade != '' and not c.isalpha():
            current_grade += c
            grades.append(current_grade)
            current_grade = ''
        elif current_grade != '' and c.isalpha():
            grades.append(current_grade)
            current_grade = c

    if current_grade != '':
        grades.append(current_grade)

    for grade in grades:
        if grade in mapping:
            points += mapping[grade]
        else:
            print('gg')

    # Write your code here.
    return None if term_grades is None or len(term_grades) == 0 or points <= 0 or len(grades) == 0 else points/len(grades)

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    print(f"Test {tc_num} : calculate_term_gpa('ACAC', {{'A':4, 'B':3, 'C':2, 'F':0}})")
    result = calculate_term_gpa('ACAC', {'A': 4, 'B': 3, 'C': 2, 'F': 0})
    print("Expected : 3.0")
    print(f"Actual   : {result}")
    print()

    print("Expected return type : <class 'float'>")
    print(f"Actual return type   : {type(result)}")  

    tc_num += 1
    print('-' * 40)
    
    print(f'''Test {tc_num}: calculate_term_gpa('A+AA-',
            {{'A+':4.3, 'A':4, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7,
            "'C+':2.3,'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'F':0}})''')
    result = calculate_term_gpa('A+AA-',
                                {'A+': 4.3, 'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                                 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0})
    print("Expected:4.0")
    print(f"Actual  :{result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    print(f"Test {tc_num}:calculate_term_gpa('A*AA',{{'A*':4, 'A':3.5, 'B*':3, 'B':2.5, 'C':2, 'F':0}})")
    result = calculate_term_gpa('A*AA',
                                {'A*': 4, 'A': 3.5, 'B*': 3, 'B': 2.5, 'C': 2, 'F': 0})
    print("Expected:3.6666666666666665")
    print(f"Actual  :{result}")
    print()
