n1, n2 = 0.0, 0.0

while n1 <= 0 or n2 <= 0 or (n1 + n2) > 100:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    if n1 <= 0 or n2 <= 0 or (n1 + n2) > 100:
        print("Conditions not satisfied!")

print("Thanks!")