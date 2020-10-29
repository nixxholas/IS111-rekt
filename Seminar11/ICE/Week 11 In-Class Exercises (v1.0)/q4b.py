stu_bd = {}

with open('students.txt') as file:
    # Name		Email ID		Birthdate		Gender
    for line in file:
        cols = line.rstrip().split('\t')
        if len(cols) > 3:
            stu_bd[cols.pop(1)] = cols

rep = True
while rep:
    email_id = input("Please enter en email ID: ")
    if email_id in stu_bd:
        print("This student is " + stu_bd[email_id][0] + ', ' + stu_bd[email_id][2] + ', born on ' + stu_bd[email_id][1] + '.')
    else:
        print("This is not a valid email ID.")
    print()
    rep = input("Do you want to continue? [Y|N]") == 'Y'
    print() if rep else print("Good-bye!")
