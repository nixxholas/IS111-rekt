import week2_utility

try:
    age = int(input("What's your age? "))
    gender = input("What's your gender? F for Female, M for Male: ")

    # Well, i don't trust whoever is keying it in..
except Exception or (age is None or age <= 0) or (gender != "F" or "M"):
    print("Please enter some proper outputs.")
    exit()

print("Your insurance premium is:", week2_utility.get_insurance_premium(age, gender))