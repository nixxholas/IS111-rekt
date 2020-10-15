while True:
    if 101 > int(input("Enter your age (between 0 and 100, both inclusive): ")) >= 0:
        print("Thanks!")
        break
    else:
        print("Please enter a valid age!")