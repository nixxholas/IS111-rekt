import random

cont_prac = True
while cont_prac:
    cont_prac = input("Do you want to practice multiplication table? Please enter Y or N: ") == "Y"

    if cont_prac:
        ran1 = random.randint(1, 9)
        ran2 = random.randint(1, 9)

        ans = int(input("What's the result of " + str(ran1) + " times " + str(ran2) + "?"))
        while ans != (ran1 * ran2):
            ans = int(input("Wrong answer! Please try again: "))
        print("You are right!")
        print()

print("Good-bye!")
