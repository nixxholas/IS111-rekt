stu_bd = {}

with open('students.txt') as file:
    # Name		Email ID		Birthdate		Gender
    for line in file:
        cols = line.rstrip().split('\t')
        if len(cols) > 3:
            stu_bd[cols[1]] = cols[2]

rep = True
while rep:
    email_id = input("Please enter en email ID: ")
    if email_id in stu_bd:
        print("The birthdate of this student is " + stu_bd[email_id])
    else:
        print("This is not a valid email ID.")
    print()
    rep = input("Do you want to continue? [Y|N]") == 'Y'
    print() if rep else print("Good-bye!")