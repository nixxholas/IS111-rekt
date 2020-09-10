plans = [(25.5, 80, 300, 100, "Combo 1"), (39.5, 200, 500, 2048, "Combo 2"), (59.5, 300, 1000, 3072, "Combo 3"),
         (79.5, 400, 1500, 4096, "Combo 4"), (109.5, 800, 2000, 10240, "Combo 5")]

print("Please tell us your monthly usage requirements.")
print()


def evaluate_requirements(outgoing, sms, data):
    for p in plans:
        if p[1] > outgoing and p[2] > sms and p[3] > (data * 1024): return p[4]
    return "Sorry! We don't have any plans that satisfy your requirements."


print("We recommend", evaluate_requirements(int(input("What's the minimum outgoing calls (in mins) you need? ")),
                      int(input("What's the minimum number of SMS/MMS you need? ")),
                      float(input("What's the minimum amount of data (in GB) you need? "))))
