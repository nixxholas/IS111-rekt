valid = ['yes', 'no']
while True:
    if input("Are you a student? ").lower() in valid:
        print("Got it!")
        break
    else:
        print("Please enter a valid answer (YES, Yes, yes, NO, No or no).")