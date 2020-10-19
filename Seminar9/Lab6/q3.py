import random

ran_num = random.randint(1, 100)
guess = 0

while guess != ran_num:
    ran_num = int(input("Enter your guess (between 1 and 100) :"))

    if ran_num > 100 or random <= 0:
        print("Please enter a number between 1 and 100.")
    elif ran_num > guess:
        print("Your guess is too low!")
    elif ran_num < guess:
        print("Your guess is too high!")

print("Bingo!")