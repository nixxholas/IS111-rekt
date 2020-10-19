while True:
    g = input("What's your gender? Please enter M or F: ")

    if g == "F" or g == "M":
        print()
        print("Thanks! Your gender is " + ("female." if g == "F" else "male."))
        break
    else:
        print("Wrong input!")
        print()